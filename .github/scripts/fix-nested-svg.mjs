// Pós-processamento dos SVGs gerados pelo readme-aura.
//
// O readme-aura "desembrulha" os <svg> internos que o Satori codifica como <image>,
// mas deixa clip-path e mask no próprio <svg x y ...>. Em navegadores, esses
// atributos passam a valer no sistema de coordenadas INTERNO do <svg>, então todo
// SVG interno que não está no canto (0,0) do bloco fica recortado e some.
// Correção: mover clip-path e mask para um <g> em volta do <svg> interno.
//
// Uso: node .github/scripts/fix-nested-svg.mjs [.github/assets]
import { readdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';

const dir = process.argv[2] ?? '.github/assets';
const nested = /<svg (x="[^"]*" y="[^"]*"[^>]*?) clip-path="(url\(#[^)]+\))" mask="(url\(#[^)]+\))">([\s\S]*?)<\/svg>/g;

let total = 0;
for (const name of await readdir(dir)) {
  if (!name.startsWith('readme-aura-component-') || !name.endsWith('.svg')) continue;
  const path = join(dir, name);
  const src = await readFile(path, 'utf8');
  let count = 0;
  const out = src.replace(nested, (_, attrs, clip, mask, body) => {
    count++;
    return `<g clip-path="${clip}" mask="${mask}"><svg ${attrs} overflow="visible">${body}</svg></g>`;
  });
  if (count) {
    await writeFile(path, out);
    total += count;
    console.log(`  ${name}: ${count} SVG(s) interno(s) corrigido(s)`);
  }
}
console.log(`fix-nested-svg: ${total} correção(ões).`);
