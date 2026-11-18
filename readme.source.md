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
     <span style={{display:'flex',fontSize:51,fontWeight:800,letterSpacing:'-2.2px',lineHeight:1.05,color:'#ffffff'}}>Eu construo IA</span>
     <span style={{display:'flex',fontSize:51,fontWeight:800,letterSpacing:'-2.2px',lineHeight:1.05,color:'#ffffff'}}>para uso real<span style={{color:'#ffffff'}}>.</span></span>
    </div>
    <span style={{display:'flex',fontSize:15,color:'#bbbbbb',marginTop:17,letterSpacing:'.15px'}}>GenAI  /  LLMs  /  Agentes  /  Automações  /  APIs</span>
    <span style={{display:'flex',fontSize:10,color:'#aaaaaa',marginTop:19,letterSpacing:'1.6px'}}>ENGENHARIA DE SOFTWARE · UCB · BRASÍLIA</span>
   </div>
  </div>
 );
})()
```

<p align="center"><strong>Desenvolvedor de IA aplicada · Engenharia de Software (UCB) · Conclusão prevista: 2027</strong></p>

<p align="center"><a href="https://www.linkedin.com/in/joaooalbernaz/">LinkedIn</a> &nbsp;·&nbsp; <a href="mailto:joaovictoralbernaz@gmail.com">E-mail</a> &nbsp;·&nbsp; <a href="https://github.com/JoaoAlbernaz1?tab=repositories">Código público</a></p>

Construo soluções de **IA generativa aplicadas a processos reais**: assistentes conversacionais, fluxos com LLMs, automações, APIs e produtos digitais. Trabalho com **Claude, OpenAI, n8n, Make, TypeScript e Python**, conectando a IA a dados, testes e experiência de uso.

### ML & Research Lab · projetos com experimentação

**Machine Learning & engenharia de IA.** Treinamento de modelos, avaliação de sistemas RAG, baselines reproduzíveis e análise de falhas.

| Experimento | Engenharia e avaliação |
| :--- | :--- |
| **[BANKING77-PTBR · NLP em dados de pesquisa](./ml-lab/banking77-ptbr/)** | **77 intenções**, 3 modelos comparados em validação, teste oficial com macro-F1 de **0,8964**. [Modelo publicado](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1) · [dashboard interativo de pesquisa](https://huggingface.co/spaces/JOAOOALBERNAZ/banking77-ptbr-research) · auditoria de sobreposição entre splits. |
| **[AI Evaluation Lab · agentes e RAG](./ml-lab/ai-evaluation-lab/)** | **32 casos de regressão**, grounding, abstinência, recuperação e ataques simulados. [Resultados medidos](./ml-lab/published/ai-eval/). |
| **[NLP · classificador de intenções](./ml-lab/nlp-intent-classifier/)** | Python, TF-IDF, Logistic Regression, macro-F1, validação cruzada; [modelo publicado no Hugging Face](https://huggingface.co/JOAOOALBERNAZ/intent-classifier-pt). |
| **[Retrieval / RAG Benchmark](./ml-lab/retrieval-benchmark/)** | Comparação BM25 × TF-IDF, Recall@k e MRR@k, embeddings multilíngues opcionais; testes reproduzíveis. |
| **[Kaggle Titanic · baseline](./ml-lab/kaggle-titanic/)** | Pipeline tabular e Random Forest; **submissão realizada** na competição Titanic. Validação cruzada local: 84,06% de acurácia (não é score do leaderboard). |
| **[Artigo técnico · avaliação de ML](./ml-lab/docs/avaliacao-reprodutivel-de-ml.md)** | Discussão sobre leakage, métricas, experimentos e limites de avaliação. |

**Pesquisas técnicas:** [BANKING77-PTBR · resultado e auditoria](./ml-lab/docs/banking77-ptbr-results.md) · [Por que recuperação correta não garante uma resposta correta](./ml-lab/docs/experimental-note-nlp-rag-2026.md) · [registro de treino com dados públicos](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44371491356).

**Kaggle:** [submissão Titanic validada no GitHub Actions](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44368002721) (ref. `58521092`) · **Hugging Face:** [intent-classifier-pt](https://huggingface.co/JOAOOALBERNAZ/intent-classifier-pt) · **artefato local:** [artefato e cartão técnico](./ml-lab/published/intent-v1/) · [métricas medidas](./ml-lab/published/intent-v1/metrics.json) · [retrieval benchmark](./ml-lab/published/retrieval-v1/metrics.json). *Resultados sobre dados sintéticos, não validação em produção.*

<sub>Experimentos documentados com resultados verificáveis; conjuntos sintéticos utilizados onde indicado. [Explorar o ML & Research Lab](./ml-lab/).</sub>

### Experiência prática com IA

```aura width=860 height=230
(function() {
 const cases=[
  {index:'01 / ASSISTENTE LEGISLATIVA',name:'Selena',status:'PROJETO PRIVADO',description:'Atendimento por WhatsApp com IA, APIs e webhooks; evolução orientada por métricas e feedback.',stack:'OpenAI   /   n8n   /   Supabase'},
  {index:'02 / LINGUAGEM NATURAL EM PRODUÇÃO',name:'Finanças Bot',status:'PROJETO PRIVADO',description:'Transforma texto em registros financeiros estruturados, com validações, prevenção de duplicidade e testes.',stack:'Claude   /   TypeScript   /   PostgreSQL'}
 ];
 return (
 <div style={{display:'flex',position:'relative',width:'100%',height:'100%',flexDirection:'column',fontFamily:'Inter',background:'#0b0b0b',border:'1px solid rgba(255,255,255,.13)',borderRadius:18,overflow:'hidden'}}>
  <style>{'@keyframes work-highlight{0%,100%{opacity:.19;transform:translateX(-20px)}50%{opacity:.54;transform:translateX(22px)}} #work-glow{animation:work-highlight 12s ease-in-out infinite}'}</style>
  <svg width="860" height="230" style={{position:'absolute',left:0,top:0}}>
   <defs><radialGradient id="work-radial"><stop offset="0%" stopColor="#c8c8c8" stopOpacity=".22"/><stop offset="100%" stopColor="#c8c8c8" stopOpacity="0"/></radialGradient></defs>
   <ellipse id="work-glow" cx="670" cy="110" rx="310" ry="190" fill="url(#work-radial)"/>
   <path d="M430 60V205" stroke="#ffffff" strokeOpacity=".16" strokeWidth="1"/>
   <path d="M38 51H821" stroke="#ffffff" strokeOpacity=".14" strokeWidth="1"/>
  </svg>
  <div style={{display:'flex',alignItems:'center',justifyContent:'space-between',position:'relative',padding:'18px 38px 16px 38px'}}>
   <span style={{display:'flex',fontSize:10,fontWeight:700,letterSpacing:'2.5px',color:'#f3f3f3'}}>SELECTED WORK</span>
   <span style={{display:'flex',fontSize:10,letterSpacing:'1.5px',color:'#999999'}}>IA APLICADA  /  2025—2026</span>
  </div>
  <div style={{display:'flex',position:'relative',width:'100%',padding:'14px 38px 22px 38px',gap:39}}>
   {cases.map(function(c){return (
    <div key={c.index} style={{display:'flex',width:350,flexDirection:'column',gap:9}}>
     <span style={{display:'flex',fontSize:10,fontWeight:700,letterSpacing:'1.1px',color:'#d0d0d0'}}>{c.index}</span>
     <span style={{display:'flex',fontSize:29,fontWeight:800,letterSpacing:'-.7px',color:'#fafafa'}}>{c.name}</span>
     <span style={{display:'flex',fontSize:12,letterSpacing:'.12px',color:'#cccccc',lineHeight:1.45}}>{c.description}</span>
     <span style={{display:'flex',fontSize:10,color:'#c4c4c4',marginTop:3}}>{c.stack}</span>
    </div>
   );})}
  </div>
 </div>
 );
})()
```

**Selena · SLCN / Senado Federal · 2025–atual — projeto privado.** Atuação no desenvolvimento e na manutenção de um assistente de atendimento via WhatsApp. Integrações com OpenAI, n8n, Supabase, APIs e webhooks; acompanhamento de métricas e feedback das interações para orientar melhorias. O código e os dados internos não são públicos.

**Finanças Bot · projeto pessoal privado.** Aplicação com Claude/Anthropic API que interpreta mensagens financeiras em português e cria registros estruturados no PostgreSQL. Inclui validação de saída, integração à WhatsApp Cloud API, verificação de assinatura, prevenção de duplicidade e testes determinísticos. Detalhamento técnico disponível em entrevista.

### Código e produtos que você pode explorar

**[UniMove — app e API de caronas universitárias](https://github.com/JoaoAlbernaz1/UniMove)**  
Aplicação colaborativa ponta a ponta com React Native/Expo, NestJS, PostgreSQL e Prisma. Desenvolvi e evoluí funcionalidades administrativas com **controle de acesso, autenticação multifator, auditoria e testes automatizados**.

**[SeuConvite IA — plataforma SaaS multi-tenant](https://github.com/JoaoAlbernaz1/seuconviteia)**  
Produto em desenvolvimento para criação de sites de eventos por subdomínio. Arquitetura com Next.js/TypeScript, isolamento multi-tenant planejado e desenvolvimento guiado por documentação e skills do Claude Code. **Ainda em evolução; não apresentado como produto concluído.**

**Curva S — acompanhamento de projetos · sistema privado**  
Painel em React e TypeScript para importação de cronogramas, comparação de avanço planejado versus realizado e visualização gerencial, com separação entre regras de cálculo e interface.

### Stack que uso na prática

| Área | Ferramentas e competências |
| :--- | :--- |
| **IA & agentes** | Claude / Anthropic API, OpenAI, LLMs, prompt engineering, saídas estruturadas, orquestração de fluxos |
| **Automações** | n8n, Make, webhooks, WhatsApp Cloud API, integrações REST |
| **Engenharia** | TypeScript, JavaScript, Python, Node.js, NestJS, FastAPI, React, Next.js, React Native / Expo |
| **Dados & qualidade** | PostgreSQL, Supabase, Prisma, Redis, Docker, GitHub Actions, Vitest, Jest, Pytest |

```aura width=860 height=95
(function(){
 return (
  <div style={{display:'flex',position:'relative',width:'100%',height:'100%',background:'#0b0b0b',borderRadius:17,overflow:'hidden',border:'1px solid rgba(255,255,255,.12)',fontFamily:'Inter',alignItems:'center',justifyContent:'space-between',padding:'0 36px'}}>
   <style>{'@keyframes contact-glow {0%,100%{transform:translateX(-90px);opacity:.2}50%{transform:translateX(90px);opacity:.65}} #contact-light{animation:contact-glow 9s ease-in-out infinite}'}</style>
   <svg width="860" height="95" style={{position:'absolute',left:0,top:0}}>
    <defs><radialGradient id="contact-halo"><stop offset="0%" stopColor="#ffffff" stopOpacity=".36"/><stop offset="100%" stopColor="#ffffff" stopOpacity="0"/></radialGradient></defs>
    <ellipse id="contact-light" cx="700" cy="80" rx="240" ry="110" fill="url(#contact-halo)"/>
   </svg>
   <div style={{display:'flex',position:'relative',flexDirection:'column',gap:7}}>
    <span style={{display:'flex',fontSize:10,letterSpacing:'2.2px',color:'#dddddd',fontWeight:700}}>BUILD / LEARN / SHIP</span>
    <span style={{display:'flex',fontSize:23,color:'#ffffff',fontWeight:800,letterSpacing:'-.6px'}}>Da ideia ao produto. Com engenharia.</span>
   </div>
   <span style={{display:'flex',position:'relative',fontSize:12,color:'#bcbcbc',letterSpacing:'.2px'}}>GENAI / AUTOMAÇÕES</span>
  </div>
 );
})()
```

<p align="center"><sub>Brasília, DF · <a href="mailto:joaovictoralbernaz@gmail.com">joaovictoralbernaz@gmail.com</a> · <a href="https://www.linkedin.com/in/joaooalbernaz/">LinkedIn</a></sub></p>

<p align="center"><sub>Componentes SVG renderizados com <a href="https://github.com/collectioneur/readme-aura">readme-aura</a> · inspiração visual em <a href="https://github.com/collectioneur">collectioneur</a></sub></p>
