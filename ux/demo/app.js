async function ask(){
  const q = document.getElementById('q').value.trim();
  const out = document.getElementById('out');
  if(!q){ return; }
  try{
    const r = await fetch('http://127.0.0.1:8000/ask',{
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({question:q})
    });
    const data = await r.json();
    out.classList.remove('hidden');
    document.getElementById('one_line').textContent = data.one_line;
    document.getElementById('answer_md').textContent = data.answer_md;
    document.getElementById('limits').textContent = data.limits;
    const src = document.getElementById('sources');
    src.innerHTML = '';
    data.sources.forEach(s=>{
      const el = document.createElement('div');
      el.innerHTML = `<strong>${s.id}</strong> ${s.title} — <em>${s.location}</em><br/><code>${s.quote}</code>`;
      src.appendChild(el);
    });
  }catch(e){
    alert('요청 오류: '+e);
  }
}
document.getElementById('ask').addEventListener('click', ask);
document.getElementById('q').addEventListener('keydown', (e)=>{ if(e.key==='Enter') ask(); });
