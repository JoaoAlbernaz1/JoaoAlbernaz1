<!-- Visual inspirado no perfil collectioneur, produzido com readme-aura. Componentes e animacoes adaptados para Joao Albernaz. -->

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
   <div style={{ display:'flex', fontSize:38, fontWeight:800, color:'#ffffff', letterSpacing:'-1px', lineHeight:1 }}>
     {'João Victor Albernaz'}
   </div>
   <div style={{ display:'flex', fontSize:15, color:'rgba(180,165,255,0.8)', fontWeight:400, letterSpacing:'0.3px' }}>
     {'Engenharia de Software · GenAI · Full-stack · Automação'}
   </div>
   <div style={{ display:'flex', gap:8, marginTop:6 }}>
     {['Python', 'TypeScript', 'React', 'n8n'].map(function(tag) {
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

```aura width=860 height=140
(function() {
 const areas = [
   {title:'Agentes de IA',detail:'LLMs  /  contextos  /  agentes',color:'#a78bfa',id:'ai'},
   {title:'Automação',detail:'n8n  /  integrações  /  APIs',color:'#60a5fa',id:'auto'},
   {title:'Produtos SaaS',detail:'Full-stack  /  experiências',color:'#67e8f9',id:'saas'}
 ];
 return (
 <div style={{
   display:'flex',position:'relative',width:'100%',height:'100%',
   fontFamily:'Inter',background:'#08080c',border:'1px solid rgba(110,80,220,0.24)',
   borderRadius:16,overflow:'hidden',flexDirection:'column'
 }}>
   <style>{String.raw`
      @keyframes aura-flow {0%{transform:translateX(-23px);opacity:0}20%{opacity:1}80%{opacity:1}100%{transform:translateX(22px);opacity:0}}
      @keyframes aura-orbit {0%,100%{transform:scale(1);opacity:.36}50%{transform:scale(1.65);opacity:.95}}
      @keyframes aura-breathe {0%,100%{opacity:.42;transform:translateX(-15px)}50%{opacity:.85;transform:translateX(28px)}}
      #focus-flow-one,#focus-flow-two{animation:aura-flow 2.8s ease-in-out infinite}
      #focus-flow-two{animation-delay:1.4s}
      #focus-orbit-ai{animation:aura-orbit 3.4s ease-in-out infinite}
      #focus-orbit-auto{animation:aura-orbit 3.4s ease-in-out infinite 1.1s}
      #focus-orbit-saas{animation:aura-orbit 3.4s ease-in-out infinite 2.2s}
      #focus-aura-glow{animation:aura-breathe 11s ease-in-out infinite}
   `}</style>
   <svg width="860" height="140" style={{position:'absolute',left:0,top:0}}>
      <defs>
        <radialGradient id="focus-violet"><stop offset="0%" stopColor="#7c3aed" stopOpacity=".32"/><stop offset="100%" stopColor="#7c3aed" stopOpacity="0"/></radialGradient>
        <radialGradient id="focus-blue"><stop offset="0%" stopColor="#2563eb" stopOpacity=".25"/><stop offset="100%" stopColor="#2563eb" stopOpacity="0"/></radialGradient>
      </defs>
      <ellipse id="focus-aura-glow" cx="330" cy="130" rx="390" ry="125" fill="url(#focus-violet)"/>
      <ellipse cx="745" cy="100" rx="260" ry="160" fill="url(#focus-blue)"/>
   </svg>
   <div style={{display:'flex',position:'relative',alignItems:'center',justifyContent:'space-between',width:'100%',padding:'14px 28px 0 28px'}}>
      <span style={{display:'flex',fontSize:10,color:'#c4b5fd',fontWeight:700,letterSpacing:'2.4px'}}>O QUE EU CONSTRUO</span>
      <span style={{display:'flex',fontSize:10,color:'rgba(195,198,222,.56)',letterSpacing:'1.4px'}}>IDEIA  →  TECNOLOGIA  →  PRODUTO</span>
   </div>
   <div style={{display:'flex',position:'relative',width:'100%',alignItems:'center',justifyContent:'center',padding:'16px 27px 0 27px'}}>
     {areas.map(function(a,i){return (
       <div key={a.id} style={{display:'flex',alignItems:'center'}}>
         <div style={{display:'flex',flexDirection:'column',width:232,height:83,borderRadius:12,background:'rgba(12,14,25,.88)',border:'1px solid rgba(125,105,220,.33)',padding:'13px 14px',gap:9}}>
           <div style={{display:'flex',alignItems:'center',gap:10}}>
             <svg width="22" height="22" viewBox="0 0 22 22">
               <circle cx="11" cy="11" r="9" fill="none" stroke={a.color} strokeOpacity=".35" strokeWidth="1.4"/>
               <circle id={'focus-orbit-'+a.id} cx="11" cy="11" r="4.1" fill={a.color} fillOpacity=".48"/>
               <circle cx="11" cy="11" r="2.1" fill={a.color}/>
             </svg>
             <span style={{display:'flex',fontSize:19,fontWeight:750,letterSpacing:'-.4px',color:'#f8f7ff'}}>{a.title}</span>
           </div>
           <span style={{display:'flex',fontSize:11,letterSpacing:'.15px',color:'#abb4cd'}}>{a.detail}</span>
         </div>
         {i<2 ? (
           <svg width="37" height="26" viewBox="0 0 37 26">
             <path d="M2 13H35" stroke="#554b83" strokeWidth="1.4" strokeDasharray="3 4"/>
             <circle id={i===0?'focus-flow-one':'focus-flow-two'} cx="18" cy="13" r="3" fill={a.color}/>
           </svg>
         ):null}
       </div>
     );})}
   </div>
 </div>
 );
})()
```

```aura width=860 height=168
(function() {
 var topLangs = github.languages.slice(0, 6).map(function(l) { return l.name; });
 var categories = [
   { title: 'Languages', color: '#a78bfa', items: topLangs },
   { title: 'Frameworks', color: '#60a5fa', items: ['React', 'Next.js', 'React Native', 'Django'] },
 ];

 return (
   <div style={{
     width: '100%', height: '100%',
     background: '#08080c',
     display: 'flex', flexDirection: 'column',
     fontFamily: 'Inter', padding: '18px 32px', gap: 14,
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

     <svg width="860" height="168" style={{ position: 'absolute', top: 0, left: 0 }}>
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
       TECH STACK
     </div>
     <div style={{ display:'flex', flexDirection:'column', gap:14 }}>
       {categories.map(function(cat) {
         return (
           <div key={cat.title} style={{ display:'flex', alignItems:'center', gap:16 }}>
             <div style={{ display:'flex', fontSize:10, fontWeight:700, color:cat.color, letterSpacing:'1px', width:80 }}>
               {cat.title.toUpperCase()}
             </div>
             <div style={{ display:'flex', flexWrap:'wrap', gap:7 }}>
               {cat.items.map(function(item) {
                 return (
                   <div key={item} style={{
                     display:'flex', padding:'4px 13px', borderRadius:6,
                     background:cat.color + '15', border:'1px solid ' + cat.color + '35',
                     color:'rgba(225,220,255,0.85)', fontSize:12, fontWeight:600,
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

```aura width=120 height=44 link="https://www.linkedin.com/in/joaooalbernaz/" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/collectioneur/collectioneur/main/icons/linkedin-icon.png"
  text="Linkedin"
  backgroundColor="#000000"
  width={120}
  height={44}
  gradientStops={[
    { offset: '0%', color: '#b57af9' },
    { offset: '30%', color: '#000000' },
    { offset: '60%', color: '#9d6bf0' },
    { offset: '80%', color: '#000000' },
    { offset: '100%', color: '#c89dfb' },
  ]}
/>
```

```aura width=138 height=44 link="https://github.com/JoaoAlbernaz1" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/JoaoAlbernaz1/JoaoAlbernaz1/main/icons/github-mark.svg"
  text="GitHub"
  backgroundColor="#000000"
  width={138}
  height={44}
  gradientStops={[
    { offset: '0%', color: '#818cf8' },
    { offset: '30%', color: '#000000' },
    { offset: '60%', color: '#9298f8' },
    { offset: '80%', color: '#000000' },
    { offset: '100%', color: '#7479f5' },
  ]}
/>
```

```aura width=110 height=44 link="mailto:joaovictoralbernaz@gmail.com" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/collectioneur/collectioneur/main/icons/gmail-icon.svg"
  text="Email"
  backgroundColor="#000000"
  width={110}
  height={44}
  gradientStops={[
    { offset: '0%', color: '#d855f7' },
    { offset: '30%', color: '#000000' },
    { offset: '60%', color: '#b557e8' },
    { offset: '80%', color: '#000000' },
    { offset: '100%', color: '#cc6ef9' },
  ]}
/>
```
 
<p align="center"><sub>Engenharia de Software · GenAI · Full-stack · Automação</sub></p>

<p align="center"><sub><a href="https://github.com/JoaoAlbernaz1/UniMove">UniMove</a> · <a href="https://github.com/JoaoAlbernaz1/seuconviteia">SeuConvite IA</a> · Selena (projeto privado) · Curva S (projeto privado)</sub></p>

<p align="center"><sub>Design baseado em <a href="https://github.com/collectioneur">collectioneur</a> · Powered by <a href="https://github.com/collectioneur/readme-aura">readme-aura</a></sub></p>
