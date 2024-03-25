
document.querySelector("#show-notification").style.display = "block";
document.querySelector("#show-notification").addEventListener("click", subscribe)

function subscribe() {
    navigator.serviceWorker.ready.then(reg => {
        reg.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: "BLWibKYf78O_trFdMew3SmmI0elBxByRzRS8eguppHvgp4MtqeVBPrYWscVQ-OgUVyVWM9aYoivNe48oVPpd-NM"
        }).then(sub => {
            console.log(JSON.parse(JSON.stringify(sub)))
            let postData = {
                user : "12345678v",
                subscription : JSON.parse(JSON.stringify(sub))
            }

            fetch('/subscribe', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(postData)
            })
        })
    })
}

if ("serviceWorker" in navigator) {
    window.addEventListener("load", function() {
      navigator.serviceWorker
        .register("serviceworker.js")
        .then(res => console.log("service worker registered"))
        .catch(err => console.log("service worker not registered", err))
    })
  }