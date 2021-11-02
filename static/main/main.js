$(document).ready(function(){
     
   $('#delete_shop').click(function(){

      $('#deleteModalLabel').html('Delete Shop');
      $('#delete_form').attr('action',"/delete_shop/"+ $('#shop_id').text());

   });

   $("#item_remove_buttton").click(function(){

      $('#deleteModalLabel').html('Delete Item');

   });

   if($('#login_message').data("login_message")){
      alertify.success($('#login_message').data("login_message"));
   }
  
   if($('#cart_message').data("cart_message")){
      alertify.success($('#cart_message').data("cart_message"));

   }

   if($('#order_message').data("order_message")){
      alertify.success($('#order_message').data("order_message"));

   }

   if($('#shop_message').data("shop_message")){
      alertify.success($('#shop_message').data("shop_message"));

   }

   if($('#login_error_message').data("login_error_message")){
      alertify.error($('#login_error_message').data("login_error_message"));

   }

   $('#add_item_form').on('submit', function(){

      var value = $("#item_image").val().toLowerCase().split('.').pop();
      
      if($.inArray(value, ['jpg', 'jpeg', 'png']) == -1 )
      {
         alertify.error('Please use only image with jpg, jpeg, png extensions');
         return false
      }
   });
   
   $('#order_form').on('submit', function(){

      var empty = true;

      $('input').each(function(){
         if($(this).val() == ""){
            empty = false
            
         }
      });
      
      if(empty == false){
         alertify.error("Please fill all the fields");
         return false
      }
      
     
      if( $('#mobile_no').val().length != 10){
         alertify.error("Mobile number should be of 10 digits");
         return false
      }
      
   });

});

function fetch(id){
   $.ajax({
            url:"/item/"+id,
            type:"GET",
            success: function(result){
               $("#update_form").attr('action','/update_item/'+result.item_id)
               $("#delete_form").attr('action','/delete_item/'+result.item_id)
               $("#update_item_name").val(result.item_name);
               $("#update_item_price").val(result.item_price);
               $("#update_item_category").val(result.item_category).change();
               $("#update_item_description").val(result.item_description);
            }


   });


}



function update_quantity(id,val){
  
   const item_id = id;
   const data =  val;
   var token = getCookie('csrftoken');
   $.ajax({
          headers:{"X-CSRFToken":token},
          url:'/update_cart/'+ item_id,
          type:'post',
          data: {'data' : data},
          success:function(result){
             $('.quantity').html(result.quantity);
             $('.total_price').html(result.total_price);
          }
   });
}

function getCookie(name) {
 var cookieValue = null;
 if (document.cookie && document.cookie !== '') {
     var cookies = document.cookie.split(';');
     for (var i = 0; i < cookies.length; i++) {
         var cookie = jQuery.trim(cookies[i]);
         // Does this cookie string begin with the name we want?
         if (cookie.substring(0, name.length + 1) === (name + '=')) {
             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
             break;
         }
     }
 }
 return cookieValue;
}

function setmainId(id){

   $('#delete_cart_form').attr('action',"/delete_cart/"+ id);

}