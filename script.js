let title = ""

function youtubeButton() {
    youtubeURL = window.prompt("Enter URL");
    console.log("URL from button is " + youtubeURL);
    // function setYouTubeURL()
    // return youtubeURL
}

function checkForNullVariable() {
    if (youtubeURL == null) {
        alert('YouTube link needs to be set.');
    }
}

// function printYouTube() {
//     console.log("URL outside function is " + youtubeURL)
// }
// printYouTube()

function changeTitle() {
    // printYouTube
    checkForNullVariable()
    console.log("URL from title is " + youtubeURL);
    jsonURL = "https://www.youtube.com/oembed?url=" + youtubeURL + "&format=json"
    console.log(jsonURL)
    console.log("Changing Title...")
    $.getJSON(jsonURL, function (data) {
        console.log(data.title)

        text = data.title
        const myArray = text.split(" - ");

        function changeToTitle() {
            document.querySelector("#title").innerText = myArray[0]
        }
        // document.querySelector("#title").innerText = myArray[0]

        changeToTitle()


        // export const title
        // document.querySelector("#title").innerText = data.title
    })
}

function changeDate() {
    checkForNullVariable()
    console.log("URL from date is " + youtubeURL);
    jsonURL = "https://www.youtube.com/oembed?url=" + youtubeURL + "&format=json"
    console.log(jsonURL)
    console.log("Changing Date...")
    $.getJSON(jsonURL, function (data) {
        console.log(data.title)

        text = data.title
        const myArray = text.split(" - ");
        //make global variable
        publishedDate = myArray[2]

        function changeToDate() {
            document.querySelector("#date").innerText = myArray[2]
        }
        // document.querySelector("#title").innerText = myArray[0]

        changeToDate()


        // export const title
        // document.querySelector("#title").innerText = data.title
    })
}

function makeImage() {
    const dataURI = canvas.toDataURL();
}

function saveImage() {
    checkForNullVariable()
    html2canvas(document.querySelector("#capture")).then(canvas => {
        // document.body.appendChild(canvas)
        // const dataURI = canvas.toDataURI();
        // imgConverted.src = dataURI

        canvas.crossOrigin = "anonymous";  // This enables CORS
        a.href.crossOrigin = "anonymous";  // This enables CORS
        a.crossOrigin = "anonymous";  // This enables CORS

        const a = document.createElement("a")

        document.body.appendChild(a);
        a.href = canvas.toDataURL();
        if (publishedDate != null) {
            a.download = publishedDate + ".png";
        } else {
            a.download = "Youtube Thumbnail.png";
        }

        // a.download = publishedDate + ".png";
        a.click();

        document.body.removeChild(a);

    });
    console.log(publishedDate)
    console.log("SCREENSHOT TAKEN")
}


// function changeTitle() {
//     document.querySelector("#title").innerText = titleArray[0]
// }
