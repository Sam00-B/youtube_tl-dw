async function getSummary() {
        const url = document.getElementById("youtubeUrl").value;
        const resultDiv = document.getElementById("result");
        const loader = document.getElementById("loader");

        if (!url) {
            alert("Please enter a YouTube URL!");
            return;
        }

        // Show loading spinner, hide the result box
        loader.style.display = "block";
        resultDiv.style.display = "none";
        resultDiv.innerHTML = "";

        try {
            // Call your Python backend
            const response = await fetch(`http://127.0.0.1:8000/summarize?url=${encodeURIComponent(url)}`);
            const data = await response.json();

            if (response.ok) {
                resultDiv.innerHTML = data.summary;
                resultDiv.style.display = "block"; // Show the box once text is ready!
            } else {
                resultDiv.innerHTML = `<span style="color: red; font-weight: bold;">Error: ${data.detail}</span>`;
                resultDiv.style.display = "block";
            }
        } catch (error) {
            resultDiv.innerHTML = `<span style="color: red; font-weight: bold;">Error connecting to the server. Is your Python backend running?</span>`;
            resultDiv.style.display = "block";
        }

        // Hide loading spinner when done
        loader.style.display = "none";
    }