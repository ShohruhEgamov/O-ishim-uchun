const modal = document.querySelector('.modal');
const call = document.querySelector('.call-top');
const closed = document.getElementById('modal-closed__X');

call.addEventListener('click', () => {
    call.style.marginLeft = '100px'
    modal.style.transform = 'translateY(0%)'
})
closed.addEventListener('click', () => {
    modal.style.display = 'none'
    call.style.marginLeft = '0'
    modal.style.transform = 'translateY(-150%)'
})


/*================================== A C C A R D I O N ==============================*/

const accardion = document.getElementsByClassName('contentbox');

for(let i = 0; i < accardion.length; i++) {
    accardion[i].addEventListener('click', function(){
        this.classList.toggle('active')
    })
}



/*================================== S L I D E R ==============================*/

// const swiper = new Swiper('.swiper', {

//     simulateTouch: false,
//     loop: true,
//     // If we need pagination
//     pagination: {
//     el: '.swiper-pagination',
//     },

//     // Navigation arrows
//     navigation: {
//         nextEl: '.swiper-button-next',
//         prevEl: '.swiper-button-prev',
//     },
    
//     // And if we need scrollbar
//     scrollbar: {
//         el: '.swiper-scrollbar',

//     },
// });

/*================================== V I D E O ==============================*/
let play = document.querySelector('.section-recommendation__left');
let vid = document.querySelector('.recommendation-video')
let remove = document.querySelector('.remove');
let playvideo = document.querySelector('.rec__image')


playvideo.addEventListener('click',() =>{
    playvideo.style.opacity = '0';
})

play.addEventListener('click',() =>{
    play.style.backgroundImage = 'none';
    vid.style.opacity = '1';
    playvideo.style.opacity = '0';
})

function playVid() { 
    vid.play();     
}



/*==================================  B E N F I T S  S L I D E R ==============================*/

$(document).ready(function() {
    $(".slide").slick({
        speed:200,
        draggable:false,
        // slidesToShow: 5,
        // slidesToScroll: 5,
        prevArrow: '<span class="prevArrow"><i class="fa-solid fa-arrow-left-long"></i></span>',
        nextArrow: '<span class="nextArrow"><i class="fa-solid fa-arrow-right-long"></i></span>'
    });

    $('.header-slider').slick({
        speed:200,
        dots:true,
        slidesToShow: 1,
        slidesToScroll: 1,
        prevArrow: '<span class="prevArrow"><i class="fa-solid fa-arrow-left-long"></i></span>',
        nextArrow: '<span class="nextArrow"><i class="fa-solid fa-arrow-right-long"></i>'
    })

    $(".slick-wrapper").slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        focusOnSelect: false,
        Infinite: true,
        speed:300,
        prevArrow: '<span class="prevArrow"><i class="fa-solid fa-arrow-left-long"></i></span>',
        nextArrow: '<span class="nextArrow"><i class="fa-solid fa-arrow-right-long"></i></span>',
        responsive: [
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                }
            }
        ]
    });


    $(".swiper-wrapper").slick({
        speed:200,
        infinite:false,
        slidesToShow: 5,
        slidesToScroll: 5,
        prevArrow: '<span class="prevArrow"><i class="fa-solid fa-arrow-left-long"></i></span>',
        nextArrow: '<span class="nextArrow"><i class="fa-solid fa-arrow-right-long"></i></span>'
    });


    $(".slider-image").slick({
        speed:200,
        prevArrow: '<span class="prevArrow"><i class="fa-solid fa-arrow-left-long"></i></span>',
        nextArrow: '<span class="nextArrow"><i class="fa-solid fa-arrow-right-long"></i></span>'
    })


    $(".question-slider").slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        speed:200,
        prevArrow: '<span class="prevArrow"><i class="fa-solid fa-arrow-left-long"></i></span>',
        nextArrow: '<span class="nextArrow"><i class="fa-solid fa-arrow-right-long"></i></span>'
    })

    $(".slider-wrapper").slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        speed:200,
        prevArrow: '<span class="prevArrow"><i class="fa-solid fa-arrow-left-long"></i></span>',
        nextArrow: '<span class="nextArrow"><i class="fa-solid fa-arrow-right-long"></i>'
    })


    $(".block-slider").slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        speed:200,
        prevArrow: '<span class="prevArrow"><i class="fa-solid fa-arrow-left-long"></i></span>',
        nextArrow: '<span class="nextArrow"><i class="fa-solid fa-arrow-right-long"></i>'
    })

})


