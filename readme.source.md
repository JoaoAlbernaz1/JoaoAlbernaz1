<!-- README de portfólio; gerado por readme-aura. Edite readme.source.md. Estilo monocromático e animações SVG com readme-aura. -->

```aura width=860 height=264
(function() {
 return (
  <div style={{display:'flex',position:'relative',width:'100%',height:'100%',background:'#090909',borderRadius:18,overflow:'hidden',border:'1px solid rgba(255,255,255,.13)',fontFamily:'Inter'}}>
   <style>{'@keyframes hero-glow {0%,100%{transform:translateX(-34px);opacity:.46}50%{transform:translateX(32px);opacity:.92}} @keyframes hero-pulse {0%,100%{opacity:.16;transform:scale(1)}50%{opacity:.64;transform:scale(1.16)}} @keyframes hero-dash {0%{stroke-dashoffset:420;opacity:.05}35%{opacity:.64}100%{stroke-dashoffset:0;opacity:.05}} #genai-glow{animation:hero-glow 11s ease-in-out infinite} #genai-halo{animation:hero-pulse 6s ease-in-out infinite} #genai-dash{animation:hero-dash 10s linear infinite}'}</style>
   <svg width="860" height="264" style={{position:'absolute',left:0,top:0}}>
    <defs>
     <radialGradient id="hero-mono-halo"><stop offset="0%" stopColor="#bbbbbb" stopOpacity=".48"/><stop offset="100%" stopColor="#bbbbbb" stopOpacity="0"/></radialGradient>
     <radialGradient id="hero-grey"><stop offset="0%" stopColor="#dddddd" stopOpacity=".11"/><stop offset="100%" stopColor="#dddddd" stopOpacity="0"/></radialGradient>
     <linearGradient id="hero-line" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stopColor="#ffffff" stopOpacity="0"/><stop offset="50%" stopColor="#ffffff" stopOpacity=".9"/><stop offset="100%" stopColor="#ffffff" stopOpacity="0"/></linearGradient>
    </defs>
    <ellipse id="genai-glow" cx="675" cy="128" rx="275" ry="235" fill="url(#hero-mono-halo)"/>
    <ellipse cx="140" cy="252" rx="390" ry="120" fill="url(#hero-grey)"/>
    <circle cx="731" cy="133" r="101" fill="none" stroke="#ffffff" strokeOpacity=".11" strokeWidth="1"/>
    <circle id="genai-halo" cx="731" cy="133" r="77" fill="none" stroke="#eeeeee" strokeOpacity=".32" strokeWidth="1.5"/>
    <circle cx="731" cy="133" r="50" fill="none" stroke="#ffffff" strokeOpacity=".16" strokeWidth="1"/>
    <path d="M634 133H827 M731 36V230" fill="none" stroke="#ffffff" strokeOpacity=".065" strokeWidth="1"/>
    <path id="genai-dash" d="M634 133H827" stroke="url(#hero-line)" strokeWidth="2" strokeDasharray="35 420"/>
    <circle cx="731" cy="133" r="4" fill="#ffffff"/>
    <rect x="40" y="31" width="26" height="3" rx="1" fill="#f4f4f4"/>
    <rect x="40" y="224" width="781" height="1" fill="#ffffff" fillOpacity=".10"/>
   </svg>
   <div style={{display:'flex',position:'relative',flexDirection:'column',padding:'42px 40px 0 40px',width:680}}>
    <span style={{display:'flex',fontSize:12,fontWeight:700,letterSpacing:'2px',color:'#dddddd'}}>JOÃO VICTOR ALBERNAZ</span>
    <div style={{display:'flex',flexDirection:'column',gap:1,marginTop:20}}>
     <span style={{display:'flex',fontSize:51,fontWeight:800,letterSpacing:'-2.2px',lineHeight:1.05,color:'#ffffff'}}>Eu desenvolvo IA</span>
     <span style={{display:'flex',fontSize:51,fontWeight:800,letterSpacing:'-2.2px',lineHeight:1.05,color:'#ffffff'}}>com engenharia<span style={{color:'#ffffff'}}>.</span></span>
    </div>
    <span style={{display:'flex',fontSize:15,color:'#bbbbbb',marginTop:17,letterSpacing:'.15px'}}>ML  /  GenAI  /  Avaliação  /  APIs</span>
    <span style={{display:'flex',fontSize:10,color:'#aaaaaa',marginTop:19,letterSpacing:'1.6px'}}>ENGENHARIA DE SOFTWARE · UCB · BRASÍLIA</span>
   </div>
  </div>
 );
})()
```

<p align="center"><strong>Engenharia de Software · UCB · Brasília, DF</strong></p>

```aura width=123 height=44 link="https://github.com/JoaoAlbernaz1" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/JoaoAlbernaz1/JoaoAlbernaz1/main/icons/github-mark.svg"
  text="GitHub"
  backgroundColor="#000000"
  textColor="#f5f5f5"
  width={123}
  height={44}
  iconSize={18}
  gradientStops={[
    { offset: '0%', color: '#cbd5e1' },
    { offset: '30%', color: '#000000' },
    { offset: '60%', color: '#94a3b8' },
    { offset: '80%', color: '#000000' },
    { offset: '100%', color: '#e2e8f0' },
  ]}
/>
```

```aura width=138 height=44 link="https://www.linkedin.com/in/joaooalbernaz/" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/JoaoAlbernaz1/JoaoAlbernaz1/main/icons/linkedin.svg"
  text="LinkedIn"
  backgroundColor="#000000"
  textColor="#f5f5f5"
  width={138}
  height={44}
  iconSize={18}
  gradientStops={[
    { offset: '0%', color: '#b57af9' },
    { offset: '30%', color: '#000000' },
    { offset: '60%', color: '#9d6bf0' },
    { offset: '80%', color: '#000000' },
    { offset: '100%', color: '#c89dfb' },
  ]}
/>
```

```aura width=169 height=44 link="https://huggingface.co/JOAOOALBERNAZ" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/JoaoAlbernaz1/JoaoAlbernaz1/main/icons/hugging-face.svg"
  text="Hugging Face"
  backgroundColor="#000000"
  textColor="#f5f5f5"
  width={169}
  height={44}
  iconSize={18}
  gradientStops={[
    { offset: '0%', color: '#ffe08a' },
    { offset: '30%', color: '#000000' },
    { offset: '60%', color: '#ffd166' },
    { offset: '80%', color: '#000000' },
    { offset: '100%', color: '#f8e7af' },
  ]}
/>
```

```aura width=125 height=44 link="https://www.kaggle.com/joaoalbernaz" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/JoaoAlbernaz1/JoaoAlbernaz1/main/icons/kaggle.svg"
  text="Kaggle"
  backgroundColor="#000000"
  textColor="#f5f5f5"
  width={125}
  height={44}
  iconSize={18}
  gradientStops={[
    { offset: '0%', color: '#5dc8f9' },
    { offset: '30%', color: '#000000' },
    { offset: '60%', color: '#7dd3fc' },
    { offset: '80%', color: '#000000' },
    { offset: '100%', color: '#4ec3f8' },
  ]}
/>
```

```aura width=117 height=44 link="mailto:joaovictoralbernaz@gmail.com" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/JoaoAlbernaz1/JoaoAlbernaz1/main/icons/email.svg"
  text="E-mail"
  backgroundColor="#000000"
  textColor="#f5f5f5"
  width={117}
  height={44}
  iconSize={18}
  gradientStops={[
    { offset: '0%', color: '#d855f7' },
    { offset: '30%', color: '#000000' },
    { offset: '60%', color: '#b557e8' },
    { offset: '80%', color: '#000000' },
    { offset: '100%', color: '#cc6ef9' },
  ]}
/>
```

Desenvolvo **Machine Learning e IA aplicada**, do treinamento de modelos a produtos com APIs, automações e testes. Gosto de transformar experimentos em software reproduzível, mensurável e útil.

### Projetos selecionados

**01 — [BANKING77-PTBR · treinamento e avaliação](./ml-lab/banking77-ptbr/)**  
Classificador de **77 intenções em português**, com comparação de três modelos e avaliação em dados públicos. **Macro-F1 0,8964** no teste oficial; **0,8910** após excluir textos idênticos ao treino.  
[Código](./ml-lab/banking77-ptbr/) · [Modelo no Hugging Face](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1) · [Resultados e limitações](./ml-lab/docs/banking77-ptbr-results.md)

**02 — [Confidence Evaluation · calibração e abstenção](./ml-lab/confidence-evaluation/)**  
Novo modelo treinado com separação entre treino, calibração e teste. **ECE 0,7844 → 0,0134**; **91,92% de acertos** nas previsões aceitas, com **94,42% de cobertura** no teste. Política experimental, não validada para produção.  
[Código](./ml-lab/confidence-evaluation/) · [Modelo publicado](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-confidence-v1) · [Artigo técnico](./ml-lab/docs/confidence-and-selective-prediction.md)

**03 — [ModelOps · inferência e monitoramento](./ml-lab/model-ops/)**  
API em **FastAPI**, Docker, testes automatizados e análise de mudança de distribuição. Um teste de erros de digitação simulados reduziu o macro-F1 de **0,8964 para 0,8502**, revelando uma limitação do classificador.  
[Código e testes](./ml-lab/model-ops/) · [Relatório de robustez](./ml-lab/published/model-ops/ROBUSTNESS.md) · [Arquitetura](./ml-lab/docs/modelops-architecture-decisions.md)

**04 — [AI Evaluation Lab · avaliação de assistentes](./ml-lab/ai-evaluation-lab/)**  
**32 casos de regressão** sobre recuperação de contexto, respostas sem evidência, abstenção e ataques simulados. Baseline extrativa com corpus fictício; os testes não representam desempenho de um LLM real.  
[Código e casos](./ml-lab/ai-evaluation-lab/) · [Resultados medidos](./ml-lab/published/ai-eval/)

### Produtos e sistemas

```aura width=860 height=377
(function(){
 const projects=[
  {num:'01',kind:'SAAS / WEB',name:'SeuConvite IA',description:'Plataforma de convites com arquitetura multi-tenant e subdomínios.',tech:'NEXT.JS   /   TYPESCRIPT',status:'EM DESENVOLVIMENTO'},
  {num:'02',kind:'MOBILE / API',name:'UniMove',description:'Aplicativo de caronas universitárias com API, acesso e testes.',tech:'REACT NATIVE   /   NESTJS',status:'CÓDIGO PÚBLICO'},
  {num:'03',kind:'LLM / AUTOMAÇÃO',name:'Selena',description:'Assistente de atendimento legislativo integrado ao WhatsApp.',tech:'LLMS   /   N8N   /   APIS',status:'PROJETO PRIVADO'},
  {num:'04',kind:'IA / DADOS',name:'Finanças Bot',description:'Transforma mensagens financeiras em registros estruturados e validados.',tech:'CLAUDE   /   POSTGRESQL',status:'PROJETO PRIVADO'}
 ];
 return (
  <div style={{position:'relative',display:'flex',flexDirection:'column',width:'100%',height:'100%',overflow:'hidden',borderRadius:17,background:'#0b0b0b',border:'1px solid rgba(255,255,255,.15)',fontFamily:'Inter'}}>
   <style>{'@keyframes board-glow {0%,100%{transform:translateX(-70px);opacity:.17}50%{transform:translateX(70px);opacity:.46}} #board-light{animation:board-glow 13s ease-in-out infinite} @keyframes board-line {0%,100%{opacity:.12}50%{opacity:.40}} #board-divider{animation:board-line 7s ease-in-out infinite}'}</style>
   <svg width="860" height="377" style={{position:'absolute',left:0,top:0}}>
    <defs><radialGradient id="project-board-halo"><stop offset="0%" stopColor="#dedede" stopOpacity=".28"/><stop offset="100%" stopColor="#dedede" stopOpacity="0"/></radialGradient></defs>
    <ellipse id="board-light" cx="720" cy="150" rx="310" ry="240" fill="url(#project-board-halo)"/>
    <path id="board-divider" d="M24 50H836" stroke="#eeeeee" strokeOpacity=".17" strokeWidth="1"/>
   </svg>
   <div style={{position:'relative',display:'flex',alignItems:'center',justifyContent:'space-between',padding:'16px 24px 12px 24px'}}>
    <span style={{display:'flex',color:'#efefef',fontSize:10,fontWeight:700,letterSpacing:'2.1px'}}>SELECTED BUILDS</span>
    <span style={{display:'flex',color:'#989898',fontSize:10,letterSpacing:'1px'}}>04 PROJETOS   /   02 PÚBLICOS</span>
   </div>
   <div style={{position:'relative',display:'flex',flexDirection:'column',gap:11,padding:'14px 24px 21px 24px'}}>
    {[projects.slice(0,2),projects.slice(2,4)].map(function(row,i){return (
     <div key={i} style={{display:'flex',gap:12,width:'100%'}}>
      {row.map(function(p){return (
       <div key={p.num} style={{display:'flex',flexDirection:'column',width:400,height:142,padding:'13px 17px 12px 17px',boxSizing:'border-box',borderRadius:11,background:'rgba(14,14,14,.82)',border:'1px solid rgba(255,255,255,.14)'}}>
        <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
         <span style={{display:'flex',color:'#d3d3d3',fontSize:9,fontWeight:700,letterSpacing:'1px'}}>{p.num}  /  {p.kind}</span>
         <span style={{display:'flex',color:'#858585',fontSize:9,letterSpacing:'.5px'}}>{p.status}</span>
        </div>
        <span style={{display:'flex',marginTop:8,fontSize:23,fontWeight:750,letterSpacing:'-.65px',lineHeight:1.15,color:'#f8f8f8'}}>{p.name}</span>
        <span style={{display:'flex',fontSize:11,lineHeight:1.45,color:'#c9c9c9',marginTop:7,minHeight:31}}>{p.description}</span>
        <span style={{display:'flex',fontSize:9,letterSpacing:'.65px',color:'#9e9e9e',marginTop:6}}>{p.tech}</span>
       </div>
      );})}
     </div>
    );})}
   </div>
  </div>
 );
})()
```

```aura width=177 height=44 link="https://github.com/JoaoAlbernaz1/seuconviteia" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/JoaoAlbernaz1/JoaoAlbernaz1/main/icons/seuconvite.svg"
  text="SeuConvite IA"
  backgroundColor="#000000"
  textColor="#f5f5f5"
  width={177}
  height={44}
  iconSize={18}
  gradientStops={[
    { offset: '0%', color: '#b57af9' },
    { offset: '30%', color: '#000000' },
    { offset: '60%', color: '#9d6bf0' },
    { offset: '80%', color: '#000000' },
    { offset: '100%', color: '#c89dfb' },
  ]}
/>
```

```aura width=144 height=44 link="https://github.com/JoaoAlbernaz1/UniMove" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/JoaoAlbernaz1/JoaoAlbernaz1/main/icons/unimove.svg"
  text="UniMove"
  backgroundColor="#000000"
  textColor="#f5f5f5"
  width={144}
  height={44}
  iconSize={18}
  gradientStops={[
    { offset: '0%', color: '#5dc8f9' },
    { offset: '30%', color: '#000000' },
    { offset: '60%', color: '#7dd3fc' },
    { offset: '80%', color: '#000000' },
    { offset: '100%', color: '#4ec3f8' },
  ]}
/>
```

**Selena** e **Finanças Bot** — projetos privados.

### Publicações e pesquisa

**Hugging Face** · [Modelos publicados](https://huggingface.co/JOAOOALBERNAZ) · [Dashboard de pesquisa](https://huggingface.co/spaces/JOAOOALBERNAZ/banking77-ptbr-research)  
**Kaggle** · [Meu perfil](https://www.kaggle.com/joaoalbernaz) · [Titanic: submissão #58521092](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44368002721) · [Pesquisa de atributos: 84,17% em CV](./ml-lab/published/kaggle-titanic-advanced/) *(nota local, não leaderboard)*  
**Artigos** · [Calibração e risco](./ml-lab/docs/confidence-and-selective-prediction.md) · [Avaliação de RAG](./ml-lab/docs/experimental-note-nlp-rag-2026.md)

**Stack:** Python · scikit-learn · FastAPI · Docker · TypeScript · Next.js · React Native · PostgreSQL · n8n · APIs de LLM.

<sub>[Todos os experimentos e métricas](./ml-lab/) · [Contato](mailto:joaovictoralbernaz@gmail.com)</sub>

