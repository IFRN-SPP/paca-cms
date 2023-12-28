// SCROLLREVEAL
window.revelar = ScrollReveal({ reset: true })

// HEADER
revelar.reveal('.hide-header', {
    easing: 'ease-in-out',
    origin: 'top',
    duration: 1000,
    opacity: null,
})


// INÍCIO
revelar.reveal('.hide-back', {
    easing: 'ease-in',
    origin: 'left',
    duration: 500,
    distance: '60%',
    scale: 0
})

revelar.reveal('.hide-front', {
    easing: 'ease-in-out',
    origin: 'top',
    duration: 1000,
    distance: '50%',
    delay: 500,
})

revelar.reveal('.hide-front2', {
    easing: 'ease-in',
    origin: 'bottom',
    duration: 1250,
    distance: '150px',
    scale: 0
})

// EQUIPE
revelar.reveal('.hide-front2', {
    easing: 'ease-in',
    origin: 'bottom',
    duration: 1250,
    distance: '150px',
    scale: 0
})