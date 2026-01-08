async function insertVector() {
    const text = document.getElementById("insert-text").value;

    if (!text) {
        alert("Text required");
        return;
    }

    const res = await fetch("/insert", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });

    const data = await res.json();
    document.getElementById("insert-status").innerText = data.status;
    document.getElementById("insert-text").value = "";
}

async function searchVectors() {
    const query = document.getElementById("search-query").value;

    if (!query) {
        alert("Query required");
        return;
    }

    const res = await fetch("/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
    });

    const data = await res.json();
    const list = document.getElementById("results");
    list.innerHTML = "";

    data.results.forEach(r => {
        const li = document.createElement("li");
        li.innerHTML = `
            ${r.text}
            <div class="score">score: ${r.score.toFixed(3)}</div>
        `;
        list.appendChild(li);
    });
}
