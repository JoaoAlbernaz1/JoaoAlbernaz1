<!-- Gerado automaticamente com collectioneur/readme-aura. Edite este arquivo, não README.md. -->
<!-- Design: inspiração no layout DarkOrbs do readme-aura, adaptado para João Albernaz. -->

```aura width=860 height=329
<div style={{display:'flex',flexDirection:'column',position:'relative',width:'100%',height:'100%',background:'linear-gradient(125deg,#163d30 0%,#151e23 29%,#221a2c 62%,#361b2c 100%)',borderRadius:19,overflow:'hidden',alignItems:'center',justifyContent:'center',fontFamily:'Inter, sans-serif'}}>
  <style>{`@keyframes hero-drift {0%,100%{opacity:.55;transform:translate(0,0)} 50%{opacity:.95;transform:translate(14px,-10px)}} @keyframes hero-drift2 {0%,100%{opacity:.6;transform:translate(0,0)} 50%{opacity:.95;transform:translate(-15px,8px)}} @keyframes hero-pulse {0%,100%{opacity:.10} 50%{opacity:.23}} #hero-a {animation:hero-drift 9s ease-in-out infinite} #hero-b {animation:hero-drift2 12s ease-in-out infinite} #hero-c {animation:hero-drift 11s ease-in-out infinite 1.2s} #hero-d {animation:hero-drift2 13s ease-in-out infinite 1.7s} @keyframes orbit {from{transform:rotate(0deg)}to{transform:rotate(360deg)}} #hero-r1 {animation:hero-pulse 7s ease-in-out infinite} #hero-r2 {animation:hero-pulse 8s ease-in-out infinite 1s} #hero-r3 {animation:hero-pulse 10s ease-in-out infinite 1.5s} #hero-orbit {animation:orbit 22s linear infinite}`}</style>
  <svg width="860" height="329" style={{position:'absolute',top:0,left:0}}>
<defs>
<radialGradient id="hero-mint"><stop offset="0%" stopColor="#3fa989" stopOpacity=".36"/><stop offset="100%" stopColor="#3fa989" stopOpacity="0"/></radialGradient>
<radialGradient id="hero-rose"><stop offset="0%" stopColor="#d65b71" stopOpacity=".34"/><stop offset="100%" stopColor="#d65b71" stopOpacity="0"/></radialGradient>
<radialGradient id="hero-violet"><stop offset="0%" stopColor="#9b78e2" stopOpacity=".34"/><stop offset="100%" stopColor="#9b78e2" stopOpacity="0"/></radialGradient>
<radialGradient id="hero-blue"><stop offset="0%" stopColor="#517ac1" stopOpacity=".25"/><stop offset="100%" stopColor="#517ac1" stopOpacity="0"/></radialGradient>
</defs>
<ellipse id="hero-a" cx="155" cy="263" rx="292" ry="227" fill="url(#hero-mint)"/>
<ellipse id="hero-b" cx="740" cy="59" rx="301" ry="234" fill="url(#hero-rose)"/>
<ellipse id="hero-c" cx="645" cy="309" rx="241" ry="184" fill="url(#hero-violet)"/>
<ellipse id="hero-d" cx="112" cy="59" rx="258" ry="181" fill="url(#hero-blue)"/>
</svg>
  <div style={{display:'flex',position:'absolute',left:329,top:45,width:202,height:202,borderRadius:101,border:'1px solid #ffffff22'}}/>
  <div style={{display:'flex',position:'absolute',left:288,top:4,width:284,height:284,borderRadius:142,border:'1px solid #ffffff15'}}/>
  <div style={{display:'flex',position:'absolute',left:236,top:-48,width:388,height:388,borderRadius:194,border:'1px solid #ffffff0d'}}/>
  <svg width="860" height="329" style={{position:'absolute',left:0,top:0}}>
    <circle id="hero-r1" cx="430" cy="157" r="63" stroke="#e9eaf4" strokeWidth=".8" fill="none"/>
    <circle id="hero-r2" cx="430" cy="157" r="112" stroke="#e9eaf4" strokeWidth=".8" fill="none"/>
    <circle id="hero-r3" cx="430" cy="157" r="169" stroke="#e9eaf4" strokeWidth=".8" fill="none"/>
    <circle cx="430" cy="157" r="230" stroke="#dde2ec" strokeOpacity=".05" strokeWidth=".8" fill="none"/>
    <g id="hero-orbit"><circle cx="430" cy="44" r="3" fill="#fff" opacity=".6"/></g>
  </svg>
  <div style={{position:'relative',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',width:'100%'}}>
    <span style={{fontSize:59,fontWeight:700,letterSpacing:-2.4,color:'#ffffff',lineHeight:1.08}}>João Albernaz</span>
    <span style={{fontSize:11,letterSpacing:4,color:'#bbc1d0',marginTop:12}}>SOFTWARE ENGINEERING  ·  GENAI  ·  AUTOMATION</span>
    <div style={{display:'flex',flexDirection:'row',gap:8,marginTop:30}}>
      {['Full-stack','AI Agents','SaaS'].map((v,i)=>(<span key={i} style={{fontSize:11,letterSpacing:.2,color:'#c8ccd8',border:'1px solid #343b49',background:'#151b2699',borderRadius:20,padding:'6px 15px'}}>{v}</span>))}
    </div>
  </div>
</div>
```

```aura width=860 height=250
<div style={{display:'flex',width:'100%',height:'100%',flexDirection:'row',gap:13,fontFamily:'Inter, sans-serif'}}>
<style>{`@keyframes ab-drift {0%,100%{opacity:.55;transform:translate(0,0)} 50%{opacity:.95;transform:translate(14px,-10px)}} @keyframes ab-drift2 {0%,100%{opacity:.6;transform:translate(0,0)} 50%{opacity:.95;transform:translate(-15px,8px)}} @keyframes ab-pulse {0%,100%{opacity:.10} 50%{opacity:.23}} #ab-a {animation:ab-drift 9s ease-in-out infinite} #ab-b {animation:ab-drift2 12s ease-in-out infinite} #ab-c {animation:ab-drift 11s ease-in-out infinite 1.2s} #ab-d {animation:ab-drift2 13s ease-in-out infinite 1.7s} @keyframes caret {0%,49%{opacity:1}50%,100%{opacity:0}} #ab-caret {animation:caret 1.1s step-end infinite}`}</style>
<div style={{display:'flex',position:'relative',flexDirection:'column',justifyContent:'center',width:574,height:250,borderRadius:17,background:'linear-gradient(130deg,#102b27 0%,#171923 46%,#41212d 100%)',overflow:'hidden',padding:'0 34px'}}>
  <svg width="574" height="250" style={{position:'absolute',top:0,left:0}}>
<defs>
<radialGradient id="ab-mint"><stop offset="0%" stopColor="#3fa989" stopOpacity=".36"/><stop offset="100%" stopColor="#3fa989" stopOpacity="0"/></radialGradient>
<radialGradient id="ab-rose"><stop offset="0%" stopColor="#d65b71" stopOpacity=".34"/><stop offset="100%" stopColor="#d65b71" stopOpacity="0"/></radialGradient>
<radialGradient id="ab-violet"><stop offset="0%" stopColor="#9b78e2" stopOpacity=".34"/><stop offset="100%" stopColor="#9b78e2" stopOpacity="0"/></radialGradient>
<radialGradient id="ab-blue"><stop offset="0%" stopColor="#517ac1" stopOpacity=".25"/><stop offset="100%" stopColor="#517ac1" stopOpacity="0"/></radialGradient>
</defs>
<ellipse id="ab-a" cx="103" cy="200" rx="195" ry="173" fill="url(#ab-mint)"/>
<ellipse id="ab-b" cx="494" cy="45" rx="201" ry="178" fill="url(#ab-rose)"/>
<ellipse id="ab-c" cx="431" cy="235" rx="161" ry="140" fill="url(#ab-violet)"/>
<ellipse id="ab-d" cx="75" cy="45" rx="172" ry="138" fill="url(#ab-blue)"/>
</svg>
  <div style={{position:'relative',display:'flex',flexDirection:'column'}}>
    <span style={{fontSize:10,color:'#bcc0d0',letterSpacing:3}}>SOBRE MIM / 01</span>
    <span style={{fontSize:28,fontWeight:700,color:'#ffffff',lineHeight:1.25,marginTop:13}}>Construindo software</span>
    <span style={{fontSize:28,fontWeight:700,color:'#ffffff',lineHeight:1.25}}>que resolve problemas.</span>
    <span style={{fontSize:14,color:'#b5becc',lineHeight:1.5,marginTop:13}}>Engenharia de Software na UCB. Desenvolvo APIs, aplicações e automações com inteligência artificial.</span>
    <div style={{display:'flex',flexDirection:'row',marginTop:15}}>
      <span style={{fontSize:12,color:'#92cab8',fontFamily:'monospace'}}>{'> open to GenAI opportunities'}</span>
      <span id="ab-caret" style={{fontSize:12,color:'#9fd3c6',marginLeft:3}}>{'_'}</span>
    </div>
  </div>
</div>
<div style={{display:'flex',flexDirection:'column',gap:13,width:273,height:250}}>
  <div style={{display:'flex',width:'100%',height:119,borderRadius:16,background:'linear-gradient(150deg,#10212c 0%,#101324 52%,#26213a 100%)',flexDirection:'column',alignItems:'center',justifyContent:'center'}}>
    <span style={{fontSize:24,fontWeight:700,color:'#e4e9f0'}}>AI / ML</span>
    <span style={{fontSize:10,color:'#bcc5d3',letterSpacing:2,marginTop:7}}>AGENTES &amp; LLMs</span>
  </div>
  <div style={{display:'flex',width:'100%',height:118,borderRadius:16,background:'linear-gradient(140deg,#1b1625,#151722 52%,#1b2c2e)',flexDirection:'column',alignItems:'center',justifyContent:'center'}}>
    <span style={{fontSize:24,fontWeight:700,color:'#e4e9f0'}}>BUILD</span>
    <span style={{fontSize:10,color:'#bcc5d3',letterSpacing:2,marginTop:7}}>LEARN · SHIP · ITERATE</span>
  </div>
</div>
</div>
```

```aura width=860 height=216
<div style={{display:'flex',position:'relative',width:'100%',height:'100%',background:'linear-gradient(115deg,#12352b 0%,#141924 38%,#2d2039 70%,#311c2b 100%)',borderRadius:17,overflow:'hidden',fontFamily:'Inter, sans-serif',alignItems:'center',justifyContent:'center',flexDirection:'column',padding:'18px 38px'}}>
  <style>{`@keyframes stack-drift {0%,100%{opacity:.55;transform:translate(0,0)} 50%{opacity:.95;transform:translate(14px,-10px)}} @keyframes stack-drift2 {0%,100%{opacity:.6;transform:translate(0,0)} 50%{opacity:.95;transform:translate(-15px,8px)}} @keyframes stack-pulse {0%,100%{opacity:.10} 50%{opacity:.23}} #stack-a {animation:stack-drift 9s ease-in-out infinite} #stack-b {animation:stack-drift2 12s ease-in-out infinite} #stack-c {animation:stack-drift 11s ease-in-out infinite 1.2s} #stack-d {animation:stack-drift2 13s ease-in-out infinite 1.7s}`}</style>
  <svg width="860" height="216" style={{position:'absolute',top:0,left:0}}>
<defs>
<radialGradient id="stack-mint"><stop offset="0%" stopColor="#3fa989" stopOpacity=".36"/><stop offset="100%" stopColor="#3fa989" stopOpacity="0"/></radialGradient>
<radialGradient id="stack-rose"><stop offset="0%" stopColor="#d65b71" stopOpacity=".34"/><stop offset="100%" stopColor="#d65b71" stopOpacity="0"/></radialGradient>
<radialGradient id="stack-violet"><stop offset="0%" stopColor="#9b78e2" stopOpacity=".34"/><stop offset="100%" stopColor="#9b78e2" stopOpacity="0"/></radialGradient>
<radialGradient id="stack-blue"><stop offset="0%" stopColor="#517ac1" stopOpacity=".25"/><stop offset="100%" stopColor="#517ac1" stopOpacity="0"/></radialGradient>
</defs>
<ellipse id="stack-a" cx="155" cy="173" rx="292" ry="149" fill="url(#stack-mint)"/>
<ellipse id="stack-b" cx="740" cy="39" rx="301" ry="153" fill="url(#stack-rose)"/>
<ellipse id="stack-c" cx="645" cy="203" rx="241" ry="121" fill="url(#stack-violet)"/>
<ellipse id="stack-d" cx="112" cy="39" rx="258" ry="119" fill="url(#stack-blue)"/>
</svg>
  <span style={{position:'relative',fontSize:11,letterSpacing:3,color:'#a3abba'}}>TECH STACK / 02</span>
  <div style={{position:'relative',display:'flex',flexWrap:'wrap',width:740,gap:8,justifyContent:'center',marginTop:20}}>
   {['Python','TypeScript','JavaScript','Java','C','React','Next.js','NestJS','PostgreSQL','Supabase','Docker','Redis','n8n','Make','Expo'].map((v,i)=>(
    <span key={i} style={{fontSize:12,letterSpacing:.2,color:'#d7dce8',border:'1px solid #434a5866',background:'#101822bc',borderRadius:18,padding:'7px 14px'}}>{v}</span>
   ))}
  </div>
  <span style={{position:'relative',fontSize:11,color:'#b5bdca',marginTop:14}}>Explorando Go e Kotlin · Foco em IA generativa e APIs</span>
</div>
```

<p align="center"><sub>Em uso: Python, TypeScript, JavaScript, Java e C. Go e Kotlin são interesses para exploração.</sub></p>

```aura width=175 height=48 link="https://github.com/JoaoAlbernaz1" inline align=center
<div style={{display:'flex',position:'relative',width:'100%',height:'100%',borderRadius:25,overflow:'hidden',background:'#0f131b',alignItems:'center',justifyContent:'center',border:'1px solid #475363'}}>
  <style>{'@keyframes edge-git {0%,100%{opacity:.22}50%{opacity:.85}} #edge-git {animation:edge-git 4.5s ease-in-out infinite}'}</style>
  <svg width="175" height="48" style={{position:'absolute',top:0,left:0}}>
    <defs><linearGradient id="button-git" x1="0%" y1="0%" x2="100%" y2="0%"><stop stopColor="#93a7c3"/><stop offset="45%" stopColor="#b1c9e6"/><stop offset="100%" stopColor="#363f55"/></linearGradient></defs>
    <rect id="edge-git" x="2" y="2" width="171" height="44" rx="22" stroke="url(#button-git)" strokeWidth="1.4" fill="none"/>
  </svg>
  <span style={{position:'relative',fontSize:13,fontWeight:600,letterSpacing:.2,color:'#f6f7fa'}}>GitHub</span>
</div>
```
```aura width=175 height=48 link="https://www.linkedin.com/in/joaooalbernaz/" inline align=center
<div style={{display:'flex',position:'relative',width:'100%',height:'100%',borderRadius:25,overflow:'hidden',background:'#0f131b',alignItems:'center',justifyContent:'center',border:'1px solid #475363'}}>
  <style>{'@keyframes edge-linkedin {0%,100%{opacity:.22}50%{opacity:.85}} #edge-linkedin {animation:edge-linkedin 4.5s ease-in-out infinite}'}</style>
  <svg width="175" height="48" style={{position:'absolute',top:0,left:0}}>
    <defs><linearGradient id="button-linkedin" x1="0%" y1="0%" x2="100%" y2="0%"><stop stopColor="#93a7c3"/><stop offset="45%" stopColor="#82aaff"/><stop offset="100%" stopColor="#363f55"/></linearGradient></defs>
    <rect id="edge-linkedin" x="2" y="2" width="171" height="44" rx="22" stroke="url(#button-linkedin)" strokeWidth="1.4" fill="none"/>
  </svg>
  <span style={{position:'relative',fontSize:13,fontWeight:600,letterSpacing:.2,color:'#f6f7fa'}}>LinkedIn</span>
</div>
```
```aura width=175 height=48 link="mailto:joaovictoralbernaz@gmail.com" inline align=center
<div style={{display:'flex',position:'relative',width:'100%',height:'100%',borderRadius:25,overflow:'hidden',background:'#0f131b',alignItems:'center',justifyContent:'center',border:'1px solid #475363'}}>
  <style>{'@keyframes edge-email {0%,100%{opacity:.22}50%{opacity:.85}} #edge-email {animation:edge-email 4.5s ease-in-out infinite}'}</style>
  <svg width="175" height="48" style={{position:'absolute',top:0,left:0}}>
    <defs><linearGradient id="button-email" x1="0%" y1="0%" x2="100%" y2="0%"><stop stopColor="#93a7c3"/><stop offset="45%" stopColor="#d49ca7"/><stop offset="100%" stopColor="#363f55"/></linearGradient></defs>
    <rect id="edge-email" x="2" y="2" width="171" height="44" rx="22" stroke="url(#button-email)" strokeWidth="1.4" fill="none"/>
  </svg>
  <span style={{position:'relative',fontSize:13,fontWeight:600,letterSpacing:.2,color:'#f6f7fa'}}>E-mail</span>
</div>
```

### Projetos em destaque

```aura width=407 height=195 inline align=center
<div style={{display:'flex',position:'relative',flexDirection:'column',background:'#0c1119',border:'1px solid #323b4a',width:'100%',height:'100%',borderRadius:16,padding:'23px 25px',fontFamily:'Inter, sans-serif',overflow:'hidden'}}>
  <svg width="407" height="195" style={{position:'absolute',left:0,top:0}}>
  <defs><radialGradient id="proj-glow"><stop stopColor="#7388ae" stopOpacity=".14"/><stop offset="100%" stopColor="#7388ae" stopOpacity="0"/></radialGradient></defs>
  <ellipse cx="349" cy="17" rx="128" ry="121" fill="url(#proj-glow)"/><circle cx="368" cy="32" r="3" fill="#b5c5ed" opacity=".8"/>
  </svg>
  <div style={{display:'flex',position:'relative',flexDirection:'row',justifyContent:'space-between',alignItems:'center'}}>
    <span style={{fontSize:10,letterSpacing:1.7,color:'#929caf'}}>PROJECT 01</span>
    <span style={{fontSize:10,letterSpacing:1,color:'#a6b2c5'}}>PRIVADO</span>
  </div>
  <span style={{position:'relative',fontSize:23,fontWeight:700,color:'#fff',marginTop:21,letterSpacing:-.5}}>Selena</span>
  <span style={{position:'relative',fontSize:13,color:'#bec6d4',lineHeight:1.4,marginTop:12}}>Assistente legislativa privada com agentes, integrações e automações.</span>
  <span style={{position:'relative',fontSize:10,letterSpacing:.4,color:'#9aa4b8',marginTop:15}}>n8n  /  LLMs  /  APIs</span>
</div>
```

```aura width=407 height=195 link="https://github.com/JoaoAlbernaz1/seuconviteia" inline align=center
<div style={{display:'flex',position:'relative',flexDirection:'column',background:'#0c1119',border:'1px solid #323b4a',width:'100%',height:'100%',borderRadius:16,padding:'23px 25px',fontFamily:'Inter, sans-serif',overflow:'hidden'}}>
  <svg width="407" height="195" style={{position:'absolute',left:0,top:0}}>
  <defs><radialGradient id="proj-glow"><stop stopColor="#7388ae" stopOpacity=".14"/><stop offset="100%" stopColor="#7388ae" stopOpacity="0"/></radialGradient></defs>
  <ellipse cx="349" cy="17" rx="128" ry="121" fill="url(#proj-glow)"/><circle cx="368" cy="32" r="3" fill="#b5c5ed" opacity=".8"/>
  </svg>
  <div style={{display:'flex',position:'relative',flexDirection:'row',justifyContent:'space-between',alignItems:'center'}}>
    <span style={{fontSize:10,letterSpacing:1.7,color:'#929caf'}}>PROJECT 02</span>
    <span style={{fontSize:10,letterSpacing:1,color:'#a6b2c5'}}>PÚBLICO</span>
  </div>
  <span style={{position:'relative',fontSize:23,fontWeight:700,color:'#fff',marginTop:21,letterSpacing:-.5}}>SeuConvite IA</span>
  <span style={{position:'relative',fontSize:13,color:'#bec6d4',lineHeight:1.4,marginTop:12}}>Plataforma SaaS multi-tenant para sites de eventos com recursos de IA.</span>
  <span style={{position:'relative',fontSize:10,letterSpacing:.4,color:'#9aa4b8',marginTop:15}}>Next.js  /  TypeScript  /  Prisma</span>
</div>
```

<!-- project row 2 -->

```aura width=407 height=195 link="https://github.com/JoaoAlbernaz1/UniMove" inline align=center
<div style={{display:'flex',position:'relative',flexDirection:'column',background:'#0c1119',border:'1px solid #323b4a',width:'100%',height:'100%',borderRadius:16,padding:'23px 25px',fontFamily:'Inter, sans-serif',overflow:'hidden'}}>
  <svg width="407" height="195" style={{position:'absolute',left:0,top:0}}>
  <defs><radialGradient id="proj-glow"><stop stopColor="#7388ae" stopOpacity=".14"/><stop offset="100%" stopColor="#7388ae" stopOpacity="0"/></radialGradient></defs>
  <ellipse cx="349" cy="17" rx="128" ry="121" fill="url(#proj-glow)"/><circle cx="368" cy="32" r="3" fill="#b5c5ed" opacity=".8"/>
  </svg>
  <div style={{display:'flex',position:'relative',flexDirection:'row',justifyContent:'space-between',alignItems:'center'}}>
    <span style={{fontSize:10,letterSpacing:1.7,color:'#929caf'}}>PROJECT 03</span>
    <span style={{fontSize:10,letterSpacing:1,color:'#a6b2c5'}}>PÚBLICO</span>
  </div>
  <span style={{position:'relative',fontSize:23,fontWeight:700,color:'#fff',marginTop:21,letterSpacing:-.5}}>UniMove</span>
  <span style={{position:'relative',fontSize:13,color:'#bec6d4',lineHeight:1.4,marginTop:12}}>Aplicativo acadêmico de caronas com API, autenticação e banco de dados.</span>
  <span style={{position:'relative',fontSize:10,letterSpacing:.4,color:'#9aa4b8',marginTop:15}}>React Native  /  Expo  /  NestJS</span>
</div>
```

```aura width=407 height=195 inline align=center
<div style={{display:'flex',position:'relative',flexDirection:'column',background:'#0c1119',border:'1px solid #323b4a',width:'100%',height:'100%',borderRadius:16,padding:'23px 25px',fontFamily:'Inter, sans-serif',overflow:'hidden'}}>
  <svg width="407" height="195" style={{position:'absolute',left:0,top:0}}>
  <defs><radialGradient id="proj-glow"><stop stopColor="#7388ae" stopOpacity=".14"/><stop offset="100%" stopColor="#7388ae" stopOpacity="0"/></radialGradient></defs>
  <ellipse cx="349" cy="17" rx="128" ry="121" fill="url(#proj-glow)"/><circle cx="368" cy="32" r="3" fill="#b5c5ed" opacity=".8"/>
  </svg>
  <div style={{display:'flex',position:'relative',flexDirection:'row',justifyContent:'space-between',alignItems:'center'}}>
    <span style={{fontSize:10,letterSpacing:1.7,color:'#929caf'}}>PROJECT 04</span>
    <span style={{fontSize:10,letterSpacing:1,color:'#a6b2c5'}}>PRIVADO</span>
  </div>
  <span style={{position:'relative',fontSize:23,fontWeight:700,color:'#fff',marginTop:21,letterSpacing:-.5}}>Curva S</span>
  <span style={{position:'relative',fontSize:13,color:'#bec6d4',lineHeight:1.4,marginTop:12}}>Painel gerencial de avanço físico, cronogramas e progresso dos projetos.</span>
  <span style={{position:'relative',fontSize:10,letterSpacing:.4,color:'#9aa4b8',marginTop:15}}>React  /  TypeScript  /  Testes</span>
</div>
```

<details>
<summary><b>Ver detalhes e outros projetos</b></summary>

**Selena:** Assistente legislativa privada com IA, n8n e integrações, incluindo fluxos internos não publicados.

**[SeuConvite IA](https://github.com/JoaoAlbernaz1/seuconviteia):** SaaS multi-tenant para eventos, autenticação e recursos opcionais de IA.

**[UniMove](https://github.com/JoaoAlbernaz1/UniMove):** Aplicativo mobile e API para caronas acadêmicas.

**Curva S:** Sistema privado de acompanhamento de projetos e comparação entre avanço planejado e realizado.

**Finanças Bot:** Assistente financeiro privado desenvolvido com TypeScript, Claude API e integração com WhatsApp.

[PartWatch](https://github.com/JoaoAlbernaz1/ddr5-radar) · [Dashboard Transporte DF](https://github.com/JoaoAlbernaz1/dashboard-onibus-df) · [Pokédex RN](https://github.com/JoaoAlbernaz1/pokedex-rn)

</details>

### Atividade no GitHub

```aura width=860 height=217
<div style={{display:'flex',position:'relative',width:'100%',height:'100%',background:'linear-gradient(120deg,#142631 0%,#141720 48%,#332642 100%)',borderRadius:17,overflow:'hidden',padding:'23px 35px',flexDirection:'column',fontFamily:'Inter, sans-serif'}}>
  <style>{`@keyframes metrics-drift {0%,100%{opacity:.55;transform:translate(0,0)} 50%{opacity:.95;transform:translate(14px,-10px)}} @keyframes metrics-drift2 {0%,100%{opacity:.6;transform:translate(0,0)} 50%{opacity:.95;transform:translate(-15px,8px)}} @keyframes metrics-pulse {0%,100%{opacity:.10} 50%{opacity:.23}} #metrics-a {animation:metrics-drift 9s ease-in-out infinite} #metrics-b {animation:metrics-drift2 12s ease-in-out infinite} #metrics-c {animation:metrics-drift 11s ease-in-out infinite 1.2s} #metrics-d {animation:metrics-drift2 13s ease-in-out infinite 1.7s}`}</style>
  <svg width="860" height="217" style={{position:'absolute',top:0,left:0}}>
<defs>
<radialGradient id="metrics-mint"><stop offset="0%" stopColor="#3fa989" stopOpacity=".36"/><stop offset="100%" stopColor="#3fa989" stopOpacity="0"/></radialGradient>
<radialGradient id="metrics-rose"><stop offset="0%" stopColor="#d65b71" stopOpacity=".34"/><stop offset="100%" stopColor="#d65b71" stopOpacity="0"/></radialGradient>
<radialGradient id="metrics-violet"><stop offset="0%" stopColor="#9b78e2" stopOpacity=".34"/><stop offset="100%" stopColor="#9b78e2" stopOpacity="0"/></radialGradient>
<radialGradient id="metrics-blue"><stop offset="0%" stopColor="#517ac1" stopOpacity=".25"/><stop offset="100%" stopColor="#517ac1" stopOpacity="0"/></radialGradient>
</defs>
<ellipse id="metrics-a" cx="155" cy="174" rx="292" ry="150" fill="url(#metrics-mint)"/>
<ellipse id="metrics-b" cx="740" cy="39" rx="301" ry="154" fill="url(#metrics-rose)"/>
<ellipse id="metrics-c" cx="645" cy="204" rx="241" ry="122" fill="url(#metrics-violet)"/>
<ellipse id="metrics-d" cx="112" cy="39" rx="258" ry="119" fill="url(#metrics-blue)"/>
</svg>
  <div style={{display:'flex',position:'relative',flexDirection:'row',justifyContent:'space-between'}}>
    <span style={{fontSize:11,letterSpacing:2.6,color:'#aab4c8'}}>GITHUB / PUBLIC ACTIVITY</span>
    <span style={{fontSize:10,letterSpacing:1.6,color:'#aab4c8'}}>{github && github.user ? github.user.login : 'JoaoAlbernaz1'}</span>
  </div>
  <div style={{display:'flex',position:'relative',flexDirection:'row',marginTop:26}}>
    {[
    ['REPOSITÓRIOS',github && github.stats ? github.stats.totalRepos : '—'],
    ['ESTRELAS',github && github.stats ? github.stats.totalStars : '—'],
    ['FORKS',github && github.stats ? github.stats.totalForks : '—']
    ].map((x,i)=>(<div key={i} style={{display:'flex',flexDirection:'column',width:250,paddingLeft:22,borderLeft:'1px solid #4a576b'}}>
      <span style={{fontSize:36,fontWeight:700,color:'#fff'}}>{String(x[1])}</span>
      <span style={{fontSize:11,color:'#c5cddd',letterSpacing:1.1,marginTop:6}}>{x[0]}</span>
    </div>))}
  </div>
  <span style={{position:'relative',fontSize:11,color:'#aab6c8',marginTop:21}}>Números dos repositórios públicos; projetos privados não incluídos.</span>
</div>
```

<div align="center">

[![Gráfico de atividade pública](https://github-readme-activity-graph.vercel.app/graph?username=JoaoAlbernaz1&bg_color=0b0e15&color=bac3d2&line=9582c8&point=b5a6ed&area=true&area_color=32314f&hide_border=true&custom_title=Atividade%20no%20GitHub)](https://github.com/JoaoAlbernaz1?tab=overview)

<sub>Gráfico externo de contribuições · [Ver atividade diretamente no GitHub](https://github.com/JoaoAlbernaz1?tab=overview)</sub>

</div>

---

<div align="center">

**João Victor Albernaz** · Engenharia de Software — UCB, Brasília

<sub>GenAI · Full-stack · Automação · Software Engineering</sub>

<sub>Design desenvolvido com [readme-aura](https://github.com/collectioneur/readme-aura), inspirado no visual de [collectioneur](https://github.com/collectioneur).</sub>

</div>
