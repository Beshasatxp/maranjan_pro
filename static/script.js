function navigateTo(pageId) {
    const pages = document.querySelectorAll('.page-section');
    pages.forEach(page => page.classList.remove('active-page'));
    const targetPage = document.getElementById(pageId);
    if(targetPage) targetPage.classList.add('active-page');
}

let slideIndex = 1;
let slideInterval;

function initSlider() {
    showSlides(slideIndex);
    startSliderTimer();
    checkUserStatus();
}

function changeSlide(n) {
    showSlides(slideIndex += n);
    resetSliderTimer();
}

function showSlides(n) {
    const slides = document.getElementsByClassName("slide");
    if (!slides.length) return;
    if (n > slides.length) { slideIndex = 1; }    
    if (n < 1) { slideIndex = slides.length; }
    for (let i = 0; i < slides.length; i++) {
        slides[i].classList.remove("active");  
    }
    slides[slideIndex - 1].classList.add("active");  
}

function startSliderTimer() {
    slideInterval = setInterval(() => { showSlides(slideIndex += 1); }, 5000);
}

function resetSliderTimer() {
    clearInterval(slideInterval);
    startSliderTimer();
}

const modal = document.getElementById("authModal");
const loginBtn = document.getElementById("loginBtn");
const signupBtn = document.getElementById("signupBtn");
const dashboardBtn = document.getElementById("dashboardBtn");
const logoutBtn = document.getElementById("logoutBtn");
const closeBtn = document.querySelector(".close");
const modalTitle = document.getElementById("modalTitle");
const authForm = document.getElementById("authForm");
let currentMode = "login";

const openModal = (title, mode) => {
    modalTitle.innerText = title;
    currentMode = mode;
    modal.style.display = "block";
    document.body.style.overflow = "hidden";
};

const closeModal = () => {
    modal.style.display = "none";
    document.body.style.overflow = "auto";
    authForm.reset();
};

loginBtn.addEventListener('click', () => openModal("تسجيل الدخول", "login"));
signupBtn.addEventListener('click', () => openModal("إنشاء حساب جديد", "signup"));
closeBtn.addEventListener('click', closeModal);

window.addEventListener('click', (event) => {
    if (event.target === modal) closeModal();
});

authForm.addEventListener('submit', async (e) => {
    e.preventDefault(); 
    const email = document.getElementById("emailInput").value;
    const password = document.getElementById("passwordInput").value;
    
    const url = currentMode === "signup" ? "/api/signup/" : "/api/login/";
    
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            closeModal();
            updateUI(true);
            navigateTo('dashboard');
            alert(data.message);
        } else {
            alert(data.message || "حدث خطأ ما!");
        }
    } catch (error) {
        alert("فشل الاتصال بالخادم!");
    }
});

logoutBtn.addEventListener('click', async () => {
    try {
        await fetch("/api/logout/", { method: 'POST' });
        updateUI(false);
        navigateTo('home');
        alert("تم تسجيل الخروج بنجاح.");
    } catch (error) {
        alert("حدث خطأ أثناء تسجيل الخروج!");
    }
});

function updateUI(isLoggedIn) {
    if (isLoggedIn) {
        loginBtn.style.display = "none";
        signupBtn.style.display = "none";
        dashboardBtn.style.display = "inline-block";
        logoutBtn.style.display = "inline-block";
    } else {
        loginBtn.style.display = "inline-block";
        signupBtn.style.display = "inline-block";
        dashboardBtn.style.display = "none";
        logoutBtn.style.display = "none";
    }
}

async function checkUserStatus() {
    try {
        const response = await fetch("/api/status/");
        const data = await response.json();
        updateUI(data.logged_in);
        if(data.logged_in) navigateTo('dashboard');
    } catch (e) {
        console.log("السيرفر غير متصل");
    }
}

window.onload = initSlider;
