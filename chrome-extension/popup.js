let cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let small = "abcdefghijklmnopqrstuvwxyz";
let num = "0123456789";
let spec = "~!@#$%^&*()_+{}|;:'/?.>,<";

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function genchar() {
    let type = getRandomInt(0, 3);

    if (type === 0) return cap[getRandomInt(0, cap.length - 1)];
    if (type === 1) return small[getRandomInt(0, small.length - 1)];
    if (type === 2) return num[getRandomInt(0, num.length - 1)];
    return spec[getRandomInt(0, spec.length - 1)];
}

let range = document.getElementById("range");
let pass = document.getElementById("pass");
let msg = document.getElementById("msg");
let copyBtn = document.getElementById("copy-btn");

// Generate on slider move
range.oninput = () => {
    let length = Number(range.value);
    let password = "";

    for (let i = 0; i < length; i++) {
        password += genchar();
    }

    pass.value = password;

    if (length <= 8) { msg.innerHTML = "Weak"; msg.style.color = "red"; }
    else if (length <= 12) { msg.innerHTML = "Normal"; msg.style.color = "yellow"; }
    else if (length <= 16) { msg.innerHTML = "Good"; msg.style.color = "greenyellow"; }
    else { msg.innerHTML = "Damn!!"; msg.style.color = "aqua"; }
};

// Auto-copy
copyBtn.onclick = async () => {
    await navigator.clipboard.writeText(pass.value);

    copyBtn.innerHTML = "✔ Copied";
    setTimeout(() => {
        copyBtn.innerHTML = `<img src="icons/copy.png"> Copy`;
    }, 1200);
};
