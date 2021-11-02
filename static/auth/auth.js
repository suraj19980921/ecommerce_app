$(document).ready(function(){

    $('#login_form').on('submit', function(e){
       
        if($('#username').val() == "" || $('#password').val() == ""){
           alertify.error('Please fill all the fields');
           return false
        }
        else{
            return true
        }     
    });

    if($('#login_messages').data()){

        alertify.success($('#login_messages').data('login_messages'));

    }

    $('#signup_form').on('submit', function(){
        
        var empty = true;

        $('input').each(function(){
            if($(this).val() == ""){
                empty = false
                }    
         });

         if(empty == false){
             alertify.error('Please fill all fields');        
             return false
         }
         else{
              
              regexp = new RegExp(/[0-9]/) 
              if(regexp.test($("#id_first_name").val()) || regexp.test($("#id_last_name").val()) ){
                alertify.error("Do not use numbers in first name or last name");
                return false
              }

              if($('#id_password1').val() != $('#id_password2').val()){
                  alertify.error("Password and confirm password not matched");
                  return false
              }

             
        }
       
    });

    if($(".errorlist li").text()){
        alertify.error($(".errorlist li").text());
    }
    






});