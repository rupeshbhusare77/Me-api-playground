const API_BASE = "http://127.0.0.1:8000";

window.onload = function() {
    loadProfile();
    loadSkills();
    loadProjects();
};

// Navigation
function showSection(section) {
    document.querySelectorAll('.content-section').forEach(sec => sec.style.display = 'none');
    document.getElementById(section + "-section").style.display = '';
}

// Profile
async function loadProfile() {
    const resp = await fetch(`${API_BASE}/profile`);
    const data = await resp.json();
    document.getElementById('profile-section').innerHTML = `
        <h2>${data.name}</h2>
        <p><b>Email:</b> ${data.email}</p>
        <p><b>Bio:</b> ${data.bio}</p>
        <p><b>Location:</b> ${data.location}</p>
        <p><b>Phone:</b> ${data.phone}</p>
        <p><b>Resume:</b> <a href="${data.resume_link}" target="_blank">View</a></p>
        <h3>Links:</h3>
        <ul>${data.links.map(link => `<li><a href="${link.url}" target="_blank">${link.platform}</a></li>`).join('')}</ul>
    `;
}

// Skills
async function loadSkills() {
    const resp = await fetch(`${API_BASE}/skills`);
    const data = await resp.json();
    document.getElementById('skills-section').innerHTML = `
        <h2>Skills</h2>
        <ul>${data.map(sk => `<li>${sk.name} (${sk.level || ''}, ${sk.years_experience || 0} yrs)</li>`).join('')}</ul>
    `;
}

// Projects
async function loadProjects() {
    const resp = await fetch(`${API_BASE}/projects`);
    const data = await resp.json();
    document.getElementById('projects-section').innerHTML = `
        <h2>Projects</h2>
        ${data.map(proj => `
            <div style="margin-bottom:18px;">
                <b>${proj.title}</b>  
                <div>${proj.description}</div>
                <div><b>Stack:</b> ${(proj.tech_stack || []).join(', ')}</div>
                <div>
                    <a href="${proj.github_link}" target="_blank">GitHub</a>
                    ${proj.live_link ? ` | <a href="${proj.live_link}" target="_blank">Live</a>` : ''}
                </div>
            </div>
        `).join('')}
    `;
}

// Search
async function runSearch() {
    const q = document.getElementById("search-input").value;
    if (!q) return;
    const resp = await fetch(`${API_BASE}/search?q=${encodeURIComponent(q)}`);
    const data = await resp.json();
    document.getElementById('search-results').innerHTML = `
        <h3>Projects:</h3>
        <ul>${data.projects.map(p => `<li>${p.title}</li>`).join('')}</ul>
        <h3>Skills:</h3>
        <ul>${data.skills.map(s => `<li>${s.name}</li>`).join('')}</ul>
    `;
}
