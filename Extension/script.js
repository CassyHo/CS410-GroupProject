const serverURL = "http://127.0.0.1:5000/";

async function fetchData(input) {
    try {
        // Use 'await' to wait for the result of the asynchronous operation
        var posts = await getResult(input);
        var linkbase = "https://campuswire.com/c/G4A2F7542/feed";
        document.getElementById("posts").innerHTML = posts.data.map(item => `<li><a href=${linkbase + item.id} target="_blank">${item.title}</a></li>`).join('');
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

function getResult(keyword) {
    var xhr = new XMLHttpRequest();

    return new Promise(function (resolve, reject) {
        xhr.open("GET", serverURL + keyword, true);
        xhr.onreadystatechange = function (e) {
            if (xhr.readyState === 4) {
            //     responseText = JSON.parse(xhr.response)
            //     resolve(responseText);
            // } else {
            //     reject(xhr.statusText);
            // }
                console.log('Full response:', xhr.responseText);
                try {
                    responseText = JSON.parse(xhr.response);
                    resolve(responseText);
                } catch (error) {
                    reject('Error parsing JSON: ' + error);
                }
            }

        };
        xhr.send();
    });
}

document.getElementById("search").onclick = async () => {
    console.log('clicked');
    var input = document.getElementById("keyword").value;
    fetchData(input);
};
