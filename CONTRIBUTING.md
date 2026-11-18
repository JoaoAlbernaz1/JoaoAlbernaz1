# Como contribuir

Obrigado pelo interesse em colaborar com este repositório. Ele reúne um perfil de desenvolvimento e o **ML & Research Lab**, com exemplos de Machine Learning, NLP, avaliação de sistemas de IA e aplicações.

Contribuições de código, testes, documentação, acessibilidade e revisões metodológicas são bem-vindas. O objetivo é publicar trabalho **reproduzível, verificável e útil**, não inflar estatísticas do GitHub.

## Encontrar uma contribuição

1. Consulte as [issues abertas](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/issues).
2. Para bugs, descreva um caso mínimo reproduzível. Para novos experimentos, explique a hipótese e o protocolo de avaliação antes de escrever código.
3. Se uma issue já estiver sendo tratada, comente sua proposta para evitar trabalhos duplicados.
4. Também é válido contribuir com testes, tipagem, documentação ou melhoria do processo de desenvolvimento.

## Preparar o ambiente

Recomendamos **Python 3.11 ou superior** para os projetos do `ml-lab`.

```bash
git clone https://github.com/JoaoAlbernaz1/JoaoAlbernaz1.git
cd JoaoAlbernaz1
python -m venv .venv
```

Ative o ambiente virtual:

- Linux/macOS: `source .venv/bin/activate`
- Windows PowerShell: `.venv\Scripts\Activate.ps1`

```bash
python -m pip install -r ml-lab/requirements.txt
python -m pytest -q ml-lab
```

Alguns experimentos exigem **dados externos, credenciais ou modelos adicionais** e não fazem parte dos testes offline. Leia o README específico de cada projeto antes de executar etapas que acessam serviços externos. Nunca publique tokens ou dados privados.

## Abrir um pull request

1. Crie um branch com nome descritivo, como `fix/modelops-input-validation` ou `docs/evaluation-protocol`.
2. Mantenha a alteração focada, com testes relevantes e uma descrição do comportamento anterior e novo.
3. Abra o PR apontando para `main` e preencha o template. Os testes do GitHub Actions devem passar.
4. Explique como reproduzir resultados, dependências e eventuais limitações. Um teste não executado deve ser identificado como tal.

**Não edite diretamente `README.md` do perfil**: ele é gerado a partir de `readme.source.md` pelo projeto `readme-aura`. Abra uma issue antes de propor grandes mudanças visuais para evitar conflitos com outras versões em análise.

## Regras para experimentos de IA

- Separe treinamento, seleção, validação e teste; evite vazamento de dados.
- Registre fonte e licença de dados, semente, número de amostras e métricas apropriadas.
- Diferencie avaliação em dados sintéticos, validação local e resultados oficiais externos.
- Não invente scores, medalhas, rankings, avaliações ou referências de submissão.
- Não faça upload de modelos, dados ou artefatos privados sem permissão.
- Documente limitações e riscos de interpretação, especialmente para LLMs e benchmarks.

## Conduta

Mantenha revisões técnicas respeitosas e objetivas. Discordâncias devem se concentrar em código, metodologia e evidências. A contribuição pode ser recusada ou solicitada para ajustes quando não cumprir esses princípios.

Para questões de segurança, **não publique credenciais nem detalhes que permitam explorar contas**. Abra um contato privado com o mantenedor antes de compartilhar informações sensíveis.
