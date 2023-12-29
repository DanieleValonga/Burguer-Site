const Toast = Swal.mixin({
    toast: true,
    position: "top-end",
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    didOpen: (toast) => {
      toast.onmouseenter = Swal.stopTimer;
      toast.onmouseleave = Swal.resumeTimer;
    }
  });
function fireTost(message) {Toast.fire({
    icon: "success",
    title: message
  })
}


document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('menu_button').addEventListener('click', function(){
        const navbar = document.getElementById('menu')

        navbar.classList.toggle('open')
    })

})

// const botao = document.querySelector('#botao');

// botao.onclick = function()