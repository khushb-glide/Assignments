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
    const list = document.getElementById("results");

    if (!query) {
        alert("Query required");
        return;
    }

    // Reset list and show a loading state
    list.innerHTML = "<li>Searching...</li>";

    try {
        const res = await fetch("/search", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query })
        });

        const data = await res.json();
        console.log("Data received from backend:", data); // Check F12 console for this!

        // Clear the list
        list.innerHTML = "";

        // Check if results are missing or empty
        if (!data.results || data.results.length === 0) {
            console.log("No results found. Updating UI...");
            // We use innerHTML directly to force the text to appear
            list.innerHTML = "<li style='color: red; font-size: 20px; font-weight: bold;'>NO RELEVANT DOCUMENTS FOUND</li>";
            return;
        }

        // Render results if they exist
        data.results.forEach(r => {
            const li = document.createElement("li");
            li.innerHTML = `<strong>${r.text}</strong><br><small>Score: ${r.score.toFixed(3)}</small><hr>`;
            list.appendChild(li);
        });

    } catch (err) {
        console.error("Fetch Error:", err);
        list.innerHTML = "<li>Error: Could not connect to backend.</li>";
    }
}