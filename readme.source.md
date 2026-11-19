<!-- Perfil de João Victor Albernaz. Fonte para readme-aura: edite este arquivo, não o README.md gerado. -->
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

Desenvolvo **produtos de software com IA aplicada**, conectando **LLMs, automações, APIs, bancos de dados e testes**. Trabalho do protótipo à arquitetura e busco evidências reproduzíveis para avaliar cada entrega.

### Em destaque · GenAI e engenharia de software

<sub>Três estudos de caso de produtos e um projeto de engenharia de ML. O código e os estágios de desenvolvimento estão identificados sem apresentar protótipos como produtos finalizados.</sub>

#### 01 — UniMove · Aplicativo, API e painel administrativo

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

**Problema:** facilitar a oferta e a busca de caronas para a comunidade universitária, com fluxos distintos de estudantes e administradores.  
**Implementação:** app em **React Native/Expo**, API **NestJS**, **PostgreSQL/Prisma**, autenticação, reservas, mensagens e painel web.  
**Evidência:** aplicativo, API e painel no mesmo repositório, com workflows de qualidade e autenticação administrativa independente com 2FA.  
**Explorar:** [Código e arquitetura](https://github.com/JoaoAlbernaz1/UniMove) · [Backend](https://github.com/JoaoAlbernaz1/UniMove/tree/main/UniMove-back) · [Protótipo de interface](https://shaky-awake-15985175.figma.site)

#### 02 — Finanças Bot · IA para linguagem natural e WhatsApp

**Problema:** registrar despesas sem exigir formulários, interpretando mensagens como “gastei 50 no mercado”.  
**Implementação:** extração estruturada por **LLM**, validação dos dados, regras de categorização em **TypeScript**, persistência em **PostgreSQL** e webhook da API oficial do **WhatsApp**.  
**Evidência:** testes no código para assinatura de mensagens, idempotência e falhas; suíte de 11 casos de aceitação com modelo real documentada, cuja execução depende de credenciais.  
**Acesso:** repositório privado; funcionalidades futuras como áudio e resumos agendados ainda não estão implementadas.

#### 03 — Selena · Assistente legislativo com IA

**Problema:** apoiar consultas e rotinas de atendimento legislativo por meio de interação conversacional.  
**Implementação:** fluxos de **n8n**, uso de **LLMs** e integração de APIs para automação e respostas orientadas ao contexto.  
**Evidência:** projeto privado de automação e IA aplicada. Código, métricas de uso e demonstração pública não estão disponíveis nesta página.

#### 04 — [ModelOps · Inferência, testes e robustez](./ml-lab/model-ops/)

**Problema:** transformar um modelo treinado em um serviço testável e acompanhar possíveis mudanças nos dados.  
**Implementação:** **FastAPI**, Docker, endpoints de inferência e health check, testes automatizados e métricas de drift.  
**Resultado medido:** no experimento com erros de digitação simulados, o macro-F1 do classificador caiu de **0,8964 para 0,8502**, demonstrando uma limitação verificável.  
**Explorar:** [API e testes](./ml-lab/model-ops/) · [Relatório de robustez](./ml-lab/published/model-ops/ROBUSTNESS.md) · [Decisões de arquitetura](./ml-lab/docs/modelops-architecture-decisions.md)

### Tecnologias

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

### Mais produtos e sistemas

<sub>Os projetos abaixo continuam no portfólio. Os botões Aura levam ao código público disponível.</sub>

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

**05 — [SeuConvite IA](https://github.com/JoaoAlbernaz1/seuconviteia)** · SaaS para convites digitais, sites de eventos e gestão multi-tenant. **Next.js, TypeScript, Prisma/PostgreSQL, autenticação e testes**. *Em desenvolvimento.* [Prévia hospedada](https://seuconviteia.vercel.app)

**06 — [PartWatch](https://github.com/JoaoAlbernaz1/ddr5-radar)** · Aplicativo para acompanhar peças de PC, preços registrados, wishlist e builds, com **Flutter/Dart** e **Supabase**. *Em desenvolvimento; comparação automática entre lojas ainda não está integrada.*

**07 — [Dashboard Ônibus DF](https://github.com/JoaoAlbernaz1/dashboard-onibus-df)** · App **React Native/Expo e TypeScript**, com navegação entre telas e indicadores. *Projeto acadêmico com dados fictícios.*

**08 — Curva S · Gestão de projetos** · Painel privado em **TypeScript** para leitura de cronogramas do MS Project, evolução planejada × realizada e análise de consistência.

**Sistema complementar — UniMove Admin** · Módulo de gestão integrado ao UniMove, com autenticação administrativa independente, gestão de usuários e revisão acadêmica. [Código público no repositório UniMove](https://github.com/JoaoAlbernaz1/UniMove/tree/main/UniMove-admin).

### Pesquisa e avaliação de Machine Learning

**[BANKING77-PTBR · classificação de intenções](./ml-lab/banking77-ptbr/)** — Experimento com **77 intenções em português** e comparação de modelos; **macro-F1 de 0,8964** no teste oficial e **0,8910** após excluir textos idênticos ao treino. [Modelo publicado](https://huggingface.co/JOAOOALBERNAZ/banking77-ptbr-intent-v1).

**[Confidence Evaluation · calibração e abstenção](./ml-lab/confidence-evaluation/)** — Separação entre treino, calibração e teste; **ECE de 0,7844 para 0,0134**, com **91,92% de acerto** nas previsões aceitas e **94,42% de cobertura** no teste. *Política experimental, não validada para produção.* [Artigo técnico](./ml-lab/docs/confidence-and-selective-prediction.md).

**[AI Evaluation Lab · avaliação de assistentes](./ml-lab/ai-evaluation-lab/)** — **32 casos de regressão** sobre recuperação de contexto, abstenção, ausência de evidência e ataques simulados. *Baseline extrativa com corpus fictício; os resultados não avaliam o desempenho de um LLM real.* [Resultados](./ml-lab/published/ai-eval/).

### Publicações e pesquisa

**Hugging Face** · [Modelos publicados](https://huggingface.co/JOAOOALBERNAZ) · [Dashboard de pesquisa](https://huggingface.co/spaces/JOAOOALBERNAZ/banking77-ptbr-research)  
**Kaggle** · [Meu perfil](https://www.kaggle.com/joaoalbernaz) · [Titanic: submissão #58521092](https://github.com/JoaoAlbernaz1/JoaoAlbernaz1/actions/runs/44368002721) · [Pesquisa de atributos: 84,17% em CV](./ml-lab/published/kaggle-titanic-advanced/) *(nota local, não leaderboard)*  
**Artigos** · [Calibração e risco](./ml-lab/docs/confidence-and-selective-prediction.md) · [Avaliação de RAG](./ml-lab/docs/experimental-note-nlp-rag-2026.md)

**Stack:** Python · scikit-learn · FastAPI · Docker · TypeScript · Next.js · React Native · PostgreSQL · n8n · APIs de LLM.

<sub>[Todos os experimentos e métricas](./ml-lab/) · [Contato](mailto:joaovictoralbernaz@gmail.com)</sub>

