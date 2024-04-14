const accardion = document.getElementsByClassName('contentbox');
const searchBar = document.querySelector('.search-bar');
const opensearch = document.querySelector('.search-menu__logo');
const adminlist = document.querySelectorAll('.listProfile-item');
const accountActive = document.querySelectorAll('.account-item__list')
const lists = document.querySelectorAll('.list-menu__item')
const burgerMenu = document.querySelector('.burger-menu');
const navburger = document.querySelector('.wrapper-nav');

// SIDEBAR ACCARDION
for(let i = 0; i < accardion.length; i++) {
    accardion[i].addEventListener('click', function(){
        this.classList.toggle('active')
    })
}


// SEARCH BAR
function removeActive() {
    searchBar.style.transform = 'translateY(-100%)'
}

opensearch.addEventListener('click', () => {
    searchBar.style.transform = 'translateY(0%)'
    window.removeEventListener('click',removeActive)
    
    searchBar.addEventListener('mouseout', () => {
        window.addEventListener('click',removeActive)
    })
})


const  searchArr = ['burger-menu','search-menu__logo','searchbar-image','btn-primary','search-menu__dashboard','search-lang','search-notifcation','search-users','profile-user'];
// window.addEventListener('click', () => {
//     for (let i = 0; i < searchArr.length; i++) {
//         if(searchArr[i] != window){
//             this.classList.toggle('active')
//         }
//     }
// })  

//  PROFILE ACTIVE 
for (let i = 0; i < adminlist.length; i++) {
    adminlist[i].addEventListener('click',function(){
        for (const iterator of adminlist) {
            iterator.classList.remove('active')
        }
        this.classList.toggle('active');
    })
}
// List active
for (let i = 0; i < lists.length; i++) {
    lists[i].addEventListener('click',function(){
        for (const iterator of lists) {
            iterator.classList.remove('active')
        }
        this.classList.toggle('active');
    })
}

// account active
for (let i = 0; i < accountActive.length; i++) {
    accountActive[i].addEventListener('click',function(){
        for (const iterator of accountActive) {
            iterator.classList.remove('active')
        }
        this.classList.toggle('active');
    })
}

// BURGER MENU
// burgerMenu.addEventListener('click', () => {
//     burgerMenu.style.transform = 'translateX(0%)'
// })

function burgerActive() {
    navburger.style.transform = 'translatex(-100%)'
}

burgerMenu.addEventListener('click', () => {
    navburger.style.transform = 'translatex(0%)'
    navburger.style.background = '#fff'
    navburger.style.zIndex = '100'
    window.removeEventListener('click',burgerActive)
    
    burgerMenu.addEventListener('mouseout', () => {
        window.addEventListener('click',burgerActive)
    })
})




