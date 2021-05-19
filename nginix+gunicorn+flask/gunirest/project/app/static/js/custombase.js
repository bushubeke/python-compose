$(document).ready(function(){
    let y=$('#base_body').height()
      let cy=$('.card').height()
      let x=$('#base_body').width()
      let fy=$('#form_body').height()
      let fx=$('#form_body').width()
      let ml=Math.round(0.5*(x-fx))+'px'
      let mt=Math.round(0.5*(y-fy))+'px'
      //console.log(ml)
      //console.log(mt)
      console.log('start')
      $('#form_body').css('margin-top',mt).css('margin-left',ml);
      //$('#email').children('input').addClass('form-control')
      //$('#password').children('input').addClass('form-control')
      //$('#remember').children('input').addClass('form-check-label')
      //$('#submit').children('input').addClass('btn btn-primary')

      $('#email').addClass('form-control')
      $('#username').addClass('form-control')
      $('#password').addClass('form-control')
      $('#remember').addClass('form-check-label')
      $('#submit').addClass('btn btn-primary')

      console.log('end')

    $( window ).resize(function() {
      let y=$('#base_body').height()
      let cy=$('.card').height()
      let x=$('#base_body').width()
      let fy=$('#form_body').height()
      let fx=$('#form_body').width()
      let ml=Math.round(0.5*(x-fx))+'px'
      let mt=Math.round(0.5*(y-fy))+'px'
      //console.log(ml)
      //console.log(mt)
      $('#form_body').css('margin-top',mt).css('margin-left',ml);
      //$('#form_body').css({"margin-top": "grey", "margin-left": "10px"});
     
    });
    
      
});
 /*
document.addEventListener("DOMContentLoaded", ()=>{
    function reportWindowSize(){
        
          console.log('faith')
          console.log('hope')
          console.log('love')
    }
    window.addEventListener('resize', reportWindowSize);

});*/

