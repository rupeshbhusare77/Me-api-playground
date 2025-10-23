const API_BASE = "me-api-playground-production-0cb4.up.railway.app";

window.onload = function () {
    loadProfile();
    loadSkills();
    loadProjects();
};

function showSection(section) {
    document.querySelectorAll(".content-section").forEach((sec) => {
        sec.classList.remove("active");
    });
    document.getElementById(section + "-section").classList.add("active");

    document.querySelectorAll("nav .nav-btn").forEach((btn) => {
        btn.classList.remove("active");
    });
    document.querySelector(
        `nav button[onclick="showSection('${section}')"]`
    ).classList.add("active");

    if (section === "search") {
        document.getElementById("search-input").focus();
    }
}

async function loadProfile() {
    const resp = await fetch(`${API_BASE}/profile`);
    const data = await resp.json();

    document.getElementById("profile-section").innerHTML = `
        <h2>${data.name}</h2>
        <p><b>Email:</b> <a href="mailto:${data.email}">${data.email}</a></p>
        <p><b>Bio:</b> ${data.bio}</p>
        <p><b>Location:</b> ${data.location}</p>
        <p><b>Phone:</b> ${data.phone}</p>
        <p><b>Resume:</b> <a href="${data.resume_link}" target="_blank">View</a></p>
        <h3>Links:</h3>
        <ul>${data.links
            .map(
                (link) =>
                    `<li><a href="${link.url}" target="_blank">${capitalize(link.platform)}</a></li>`
            )
            .join("")}</ul>
    `;
}

async function loadSkills() {
    const resp = await fetch(`${API_BASE}/skills`);
    const data = await resp.json();

    document.getElementById(
        "skills-section"
    ).innerHTML = `<h2>Skills</h2><ul>${data
        .map(
            (sk) =>
                `<li>${sk.name}</li>`
        )
        .join("")}</ul>`;

}

async function loadProjects() {
    const resp = await fetch(`${API_BASE}/projects`);
    const data = await resp.json();

    document.getElementById("projects-section").innerHTML = `<h2>Projects</h2>${data
        .map(
            (proj) => `
        <div class="project-card">
            <h3>${proj.title}</h3>
            <p>${proj.description || ""}</p>
            <p class="project-stack">Tech Stack: ${(proj.tech_stack || []).join(
                ", "
            )}</p>
            <p class="project-links">
                <a href="${proj.github_link}" target="_blank">GitHub</a> ${proj.live_link
                    ? ` | <a href="${proj.live_link}" target="_blank">Live</a>`
                    : ""
                }
            </p>
        </div>`
        )
        .join("")}`;
}

async function runSearch() {
    const q = document.getElementById("search-input").value.trim();
    if (!q) return;

    const resp = await fetch(`${API_BASE}/search?q=${encodeURIComponent(q)}`);
    const data = await resp.json();

    document.getElementById("search-results").innerHTML = `
        <h3>Projects:</h3>
        <ul>${data.projects.map((p) => `<li>${p.title}</li>`).join("")}</ul>
        <h3>Skills:</h3>
        <ul>${data.skills.map((s) => `<li>${s.name}</li>`).join("")}</ul>
    `;
}

function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}
