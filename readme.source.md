<!-- README de portfólio: estrutura em 3 painéis Aurora inspirada no perfil Collectioneur; gerado por readme-aura. Edite readme.source.md. -->

```aura width=860 height=200
 <div style={{
 width: '100%', height: '100%', background: '#08080c',
 display: 'flex', alignItems: 'center', fontFamily: 'Inter',
 position: 'relative', overflow: 'hidden', borderRadius: 16,
 border: '1px solid rgba(110,80,220,0.18)'
}}>

 <style>
   {`
     @keyframes float-slow {
       0%, 100% { transform: translateX(0px); opacity: 0.8; }
       50% { transform: translateX(350px); opacity: 1.2; }
     }
     @keyframes float-medium {
       0%, 100% { transform: translateX(0px); opacity: 0.7; }
       50% { transform: translateX(-250px); opacity: 1.1; }
     }
     @keyframes float-fast {
       0%, 100% { transform: translateX(0px); opacity: 0.9; }
       50% { transform: translateX(200px); opacity: 0.6; }
     }
     @keyframes float-diagonal {
       0%, 100% { transform: translateX(0px); opacity: 0.75; }
       50% { transform: translateX(300px); opacity: 1.0; }
     }
     @keyframes float-wave {
       0%, 100% { transform: translateX(0px); opacity: 0.65; }
       33% { transform: translateX(-160px); opacity: 0.9; }
       66% { transform: translateX(80px); opacity: 1.0; }
     }
     @keyframes float-pulse {
       0%, 100% { transform: scale(1); opacity: 0.8; }
       50% { transform: scale(1.3); opacity: 0.4; }
     }
     #glow-1 { animation: float-slow 8s ease-in-out infinite; }
     #glow-2 { animation: float-medium 12s ease-in-out infinite; }
     #glow-3 { animation: float-fast 9s ease-in-out infinite; }
     #glow-4 { animation: float-slow 11s ease-in-out infinite reverse; }
     #glow-5 { animation: float-medium 14s ease-in-out infinite reverse; }
     #glow-6 { animation: float-diagonal 10s ease-in-out infinite; }
     #glow-7 { animation: float-wave 13s ease-in-out infinite; }
     #glow-8 { animation: float-pulse 7s ease-in-out infinite; }
   `}
 </style>

 <svg width="860" height="200" style={{ position: 'absolute', top: 0, left: 0 }}>
   <defs>
     <radialGradient id="g1" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(110,20,210,0.72)" />
       <stop offset="40%" stopColor="rgba(90,15,180,0.35)" />
       <stop offset="70%" stopColor="rgba(90,15,180,0)" />
     </radialGradient>
     <radialGradient id="g2" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(40,60,255,0.6)" />
       <stop offset="45%" stopColor="rgba(30,50,200,0.25)" />
       <stop offset="70%" stopColor="rgba(30,50,200,0)" />
     </radialGradient>
     <radialGradient id="g3" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(0,130,255,0.45)" />
       <stop offset="50%" stopColor="rgba(0,100,220,0.18)" />
       <stop offset="70%" stopColor="rgba(0,100,220,0)" />
     </radialGradient>
     <radialGradient id="g4" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(0,190,230,0.32)" />
       <stop offset="70%" stopColor="rgba(0,190,230,0)" />
     </radialGradient>
     <radialGradient id="g5" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(90,30,200,0.38)" />
       <stop offset="70%" stopColor="rgba(90,30,200,0)" />
     </radialGradient>
     <radialGradient id="g6" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(160,30,255,0.55)" />
       <stop offset="45%" stopColor="rgba(130,20,220,0.22)" />
       <stop offset="70%" stopColor="rgba(130,20,220,0)" />
     </radialGradient>
     <radialGradient id="g7" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(20,60,255,0.42)" />
       <stop offset="50%" stopColor="rgba(10,40,200,0.16)" />
       <stop offset="70%" stopColor="rgba(10,40,200,0)" />
     </radialGradient>
     <radialGradient id="g8" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(0,170,255,0.40)" />
       <stop offset="50%" stopColor="rgba(0,130,220,0.15)" />
       <stop offset="70%" stopColor="rgba(0,130,220,0)" />
     </radialGradient>
   </defs>

   <ellipse id="glow-1" cx="180" cy="230" rx="260" ry="190" fill="url(#g1)" />
   <ellipse id="glow-2" cx="300" cy="240" rx="220" ry="160" fill="url(#g2)" />
   <ellipse id="glow-3" cx="420" cy="240" rx="180" ry="140" fill="url(#g3)" />
   <ellipse id="glow-4" cx="550" cy="250" rx="150" ry="120" fill="url(#g4)" />
   <ellipse id="glow-5" cx="750" cy="250" rx="130" ry="110" fill="url(#g5)" />
   <ellipse id="glow-6" cx="300" cy="240" rx="180" ry="140" fill="url(#g6)" />
   <ellipse id="glow-7" cx="490" cy="230" rx="220" ry="170" fill="url(#g7)" />
   <ellipse id="glow-8" cx="590" cy="250" rx="150" ry="130" fill="url(#g8)" />
 </svg>

 <div style={{
   position: 'absolute', left: 48, top: 52, width: 96, height: 96,
   borderRadius: 48, background: 'linear-gradient(135deg, #6622ee, #0088ff)',
   display: 'flex', alignItems: 'center', justifyContent: 'center',
 }}>
   <img src={github.user.avatarUrl} width={88} height={88} style={{ borderRadius: 44 }} />
 </div>

 <div style={{ display:'flex', flexDirection:'column', marginLeft:168, gap:8, zIndex: 10 }}>
   <div style={{ display:'flex', fontSize:37, fontWeight:800, color:'#ffffff', letterSpacing:'-1px', lineHeight:1 }}>
     {'João Victor Albernaz'}
   </div>
   <div style={{ display:'flex', fontSize:15, color:'rgba(180,165,255,0.8)', fontWeight:400, letterSpacing:'0.3px' }}>
     {'Engenharia de Software · IA aplicada · Brasília, DF'}
   </div>
   <div style={{ display:'flex', gap:8, marginTop:6 }}>
     {['Python', 'GenAI', 'Next.js', 'React Native'].map(function(tag) {
       return (
         <div key={tag} style={{
           display:'flex', padding:'4px 12px', borderRadius:20,
           background:'rgba(80,40,220,0.18)', border:'1px solid rgba(100,70,240,0.32)',
           color:'rgba(205,195,255,0.85)', fontSize:12, fontWeight:600,
         }}>{tag}</div>
       );
     })}
   </div>
 </div>
</div>
```

```aura width=860 height=226
(function() {
 var categories = [
   { title: 'Languages', color: '#a78bfa', items: ['TypeScript', 'Python', 'JavaScript'] },
   { title: 'GenAI & Agents', color: '#c084fc', items: ['Claude', 'OpenAI', 'LLMs', 'n8n', 'Make'] },
   { title: 'ML & Evaluation', color: '#60a5fa', items: ['scikit-learn', 'Hugging Face', 'Pytest'] },
   { title: 'Backend & DevOps', color: '#67e8f9', items: ['NestJS', 'FastAPI', 'PostgreSQL', 'Docker', 'GitHub Actions'] },
 ];

 return (
   <div style={{
     width: '100%', height: '100%',
     background: '#08080c',
     display: 'flex', flexDirection: 'column',
     fontFamily: 'Inter', padding: '18px 30px', gap: 12,
     borderRadius: 16, border: '1px solid rgba(110,80,220,0.18)',
     position: 'relative', overflow: 'hidden',
   }}>

     <style>
       {`
         @keyframes float-slow {
           0%, 100% { transform: translateX(0px); opacity: 0.8; }
           50% { transform: translateX(350px); opacity: 1.2; }
         }
         @keyframes float-medium {
           0%, 100% { transform: translateX(0px); opacity: 0.7; }
           50% { transform: translateX(-250px); opacity: 1.1; }
         }
         @keyframes float-fast {
           0%, 100% { transform: translateX(0px); opacity: 0.9; }
           50% { transform: translateX(200px); opacity: 0.6; }
         }
         @keyframes float-diagonal {
           0%, 100% { transform: translate(0px, 0px); opacity: 0.75; }
           50% { transform: translate(120px, 30px); opacity: 1.0; }
         }
         @keyframes float-wave {
           0%, 100% { transform: translateX(0px); opacity: 0.65; }
           33% { transform: translateX(-160px); opacity: 0.9; }
           66% { transform: translateX(80px); opacity: 1.0; }
         }
         @keyframes float-pulse {
           0%, 100% { transform: scale(1); opacity: 0.8; }
           50% { transform: scale(1.3); opacity: 0.4; }
         }
         #glow-1 { animation: float-slow 9s ease-in-out infinite; }
         #glow-2 { animation: float-medium 12s ease-in-out infinite; }
         #glow-3 { animation: float-fast 8s ease-in-out infinite; }
         #glow-4 { animation: float-diagonal 11s ease-in-out infinite reverse; }
         #glow-5 { animation: float-wave 14s ease-in-out infinite reverse; }
         #glow-6 { animation: float-pulse 6s ease-in-out infinite; }
       `}
     </style>

     <svg width="860" height="226" style={{ position: 'absolute', top: 0, left: 0 }}>
       <defs>
         <radialGradient id="g1" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(115,20,215,0.68)" />
           <stop offset="42%" stopColor="rgba(85,15,175,0.30)" />
           <stop offset="70%" stopColor="rgba(85,15,175,0)" />
         </radialGradient>
         <radialGradient id="g2" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(55,55,255,0.55)" />
           <stop offset="45%" stopColor="rgba(35,45,210,0.22)" />
           <stop offset="70%" stopColor="rgba(35,45,210,0)" />
         </radialGradient>
         <radialGradient id="g3" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(0,130,255,0.42)" />
           <stop offset="50%" stopColor="rgba(0,100,220,0.16)" />
           <stop offset="70%" stopColor="rgba(0,100,220,0)" />
         </radialGradient>
         <radialGradient id="g4" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(0,185,240,0.32)" />
           <stop offset="70%" stopColor="rgba(0,185,240,0)" />
         </radialGradient>
         <radialGradient id="g5" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(100,25,205,0.42)" />
           <stop offset="70%" stopColor="rgba(100,25,205,0)" />
         </radialGradient>
         <radialGradient id="g6" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(60,80,255,0.35)" />
           <stop offset="70%" stopColor="rgba(60,80,255,0)" />
         </radialGradient>
       </defs>
       <ellipse id="glow-1" cx="170" cy="168" rx="260" ry="170" fill="url(#g1)" />
       <ellipse id="glow-2" cx="320" cy="178" rx="220" ry="140" fill="url(#g2)" />
       <ellipse id="glow-3" cx="460" cy="178" rx="190" ry="130" fill="url(#g3)" />
       <ellipse id="glow-4" cx="590" cy="188" rx="160" ry="110" fill="url(#g4)" />
       <ellipse id="glow-5" cx="750" cy="188" rx="140" ry="100" fill="url(#g5)" />
       <ellipse id="glow-6" cx="420" cy="138" rx="100" ry="80" fill="url(#g6)" />
     </svg>

     <div style={{ display:'flex', fontSize:10, fontWeight:700, color:'rgba(155,140,210,0.5)', letterSpacing:'3px' }}>
       TECH STACK   /   AI ENGINEERING
     </div>
     <div style={{ display:'flex', flexDirection:'column', gap:10 }}>
       {categories.map(function(cat) {
         return (
           <div key={cat.title} style={{ display:'flex', alignItems:'center', gap:10 }}>
             <div style={{ display:'flex', fontSize:10, fontWeight:700, color:cat.color, letterSpacing:'1px', width:138 }}>
               {cat.title.toUpperCase()}
             </div>
             <div style={{ display:'flex', flexWrap:'wrap', gap:6 }}>
               {cat.items.map(function(item) {
                 return (
                   <div key={item} style={{
                     display:'flex', padding:'4px 11px', borderRadius:6,
                     background:cat.color + '15', border:'1px solid ' + cat.color + '35',
                     color:'rgba(225,220,255,0.85)', fontSize:11, fontWeight:600,
                   }}>{item}</div>
                 );
               })}
             </div>
           </div>
         );
       })}
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

<sub>Projetos de software com foco em IA aplicada, engenharia de produtos, APIs e automações. Repositórios privados permanecem identificados como privados.</sub>

**Em destaque · IA aplicada e automações**

**01 — Selena · Assistente legislativo** — Assistente privado de IA conversacional integrado a fluxos de automação e atendimento legislativo com LLMs, n8n e APIs.

**02 — Finanças Bot · IA financeira** — Sistema privado em TypeScript que usa modelos de linguagem para estruturar lançamentos financeiros em português, classificar registros no PostgreSQL e processar mensagens via webhook do WhatsApp.

**Engenharia de IA · código e avaliação reproduzível**

[**ModelOps · API de inferência, Docker e robustez**](./ml-lab/model-ops/) — Serviço com FastAPI, testes automatizados e avaliação de mudança de distribuição em entradas de texto.

[**AI Evaluation Lab · testes de agentes e assistentes**](./ml-lab/ai-evaluation-lab/) — 32 casos de regressão sobre recuperação de contexto, abstenção e resistência a instruções adversariais. *Baseline experimental com corpus fictício, não avaliação de um LLM real.*

**Produtos com código público**

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

```aura width=154 height=44 link="https://github.com/JoaoAlbernaz1/ddr5-radar" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/JoaoAlbernaz1/JoaoAlbernaz1/main/icons/partwatch.svg"
  text="PartWatch"
  backgroundColor="#000000"
  textColor="#f5f5f5"
  width={154}
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

```aura width=151 height=44 link="https://github.com/JoaoAlbernaz1/dashboard-onibus-df" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/JoaoAlbernaz1/JoaoAlbernaz1/main/icons/onibus-df.svg"
  text="Ônibus DF"
  backgroundColor="#000000"
  textColor="#f5f5f5"
  width={151}
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

**03 — SeuConvite IA** · SaaS de convites e sites para eventos, com Next.js, TypeScript, estrutura multi-tenant, autenticação e integrações. *Em desenvolvimento.*

**04 — UniMove** · App mobile e painel web com React Native, NestJS, PostgreSQL, API REST, autenticação e testes.

**05 — PartWatch** · Aplicativo de histórico de preços de peças de PC, wishlist, registro de alertas e builds. *Em desenvolvimento; comparador multi-loja ainda não integrado.*

**06 — Dashboard Ônibus DF** · Aplicativo React Native com painéis de indicadores e navegação. *Protótipo acadêmico com dados fictícios.*

**Outros sistemas**

**07 — Curva S · Gestão de projetos** — Painel privado em TypeScript para análise de cronogramas do MS Project, curvas de avanço físico e validação de dados.

**08 — UniMove Admin · Gestão e segurança** — Módulo administrativo do UniMove com autenticação independente, controle de usuários e fluxos de revisão.

<sub>Os oito produtos e sistemas foram mantidos. Os casos de engenharia de IA acima são trabalhos técnicos adicionais. Projetos privados não possuem links públicos; protótipos e sistemas em desenvolvimento não são apresentados como serviços prontos para produção.</sub>

### Publicações e pesquisa

**Hugging Face** · [Modelos publicados](https://huggingface.co/JOAOOALBERNAZ) · [Dashboard de pesquisa](https://huggingface.co/spaces/JOAOOALBERNAZ/banking77-ptbr-research)  
**Kaggle** · [Meu perfil](https://www.kaggle.com/joaoalbernaz) · [Titanic: submissão #58521092](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44368002721) · [Pesquisa de atributos: 84,17% em CV](./ml-lab/published/kaggle-titanic-advanced/) *(nota local, não leaderboard)*  
**Artigos** · [Calibração e risco](./ml-lab/docs/confidence-and-selective-prediction.md) · [Avaliação de RAG](./ml-lab/docs/experimental-note-nlp-rag-2026.md)

**Stack:** Python · scikit-learn · FastAPI · Docker · TypeScript · Next.js · React Native · PostgreSQL · n8n · APIs de LLM.

<sub>[Todos os experimentos e métricas](./ml-lab/) · [Contato](mailto:joaovictoralbernaz@gmail.com)</sub>

