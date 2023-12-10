
// Server URL for making requests
const serverURL = "http://127.0.0.1:5000/";

// Asynchronous function to fetch data from the server based on the input keyword
async function fetchData(input) {
    try {
        // Use 'await' to wait for the result of the asynchronous operation
        var posts = await getResult(input);

        // base URL for constructing post links
        var linkbase = "https://campuswire.com/c/G4A2F7542/feed/";

        // update the HTML content of the posts element with the fetched data
        document.getElementById("posts").innerHTML = posts.data.map(item => `<li>
                                               <a href=${linkbase + item.id} target="_blank">${item.title}</a>
                                               ${"--"+item.likes+" likes"}</li>`).join('');
        
    } catch (error) {
        // log the errors that occur during fetching
        console.error("Error fetching data:", error);
    }
}

// function to make an XMLHttpRequest to the server and return a Promise
function getResult(keyword) {
    // create a new instance of XMLHttpRequest
    var xhr = new XMLHttpRequest();

    // return a promise
    return new Promise(function (resolve, reject) {

        // Configure the XMLHttpRequest with the method, URL, and asynchronous flag
        xhr.open("GET", serverURL + keyword, true);

        // set up an event listener for state change
        xhr.onreadystatechange = function (e) {
            // check if the request is complete
            if (xhr.readyState === 4) {
                // log the full response
                console.log('Full response:', xhr.responseText);
                try {
                    // parse response text as JSON
                    responseText = JSON.parse(xhr.response);
                    // resolve the promise with the parsed JSON
                    resolve(responseText);
                } catch (error) {
                    // If paring fails then reject the promise with an error message
                    reject('Error parsing JSON: ' + error);
                }
            }

        };
        // send the XMLHttpRequest
        xhr.send();
    });
}

// event handler for the search button click
document.getElementById("search").onclick = async () => {
    console.log('clicked');

    // get the input value from the keyword field
    var input = document.getElementById("keyword").value;

    // call the  fetchData function
    fetchData(input);
};
