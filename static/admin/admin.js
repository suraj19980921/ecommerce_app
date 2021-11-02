$(document).ready(function(){

    if($('#delete_user_message').data("delete_user_message")){
        alertify.success($('#delete_user_message').data("delete_user_message"));
     }
    
    if($('#delete_cart_message').data("delete_cart_message")){
        alertify.success($('#delete_cart_message').data("delete_cart_message"));
    }

    if($('#delete_category_message').data("delete_category_message")){
        alertify.success($('#delete_category_message').data("delete_category_message"));
    }

    if($('#admin_item_message').data("admin_item_message")){
        alertify.success($('#admin_item_message').data("admin_item_message"));
    }

    if($('#admin_order_message').data("admin_order_message")){
        alertify.success($('#admin_order_message').data("admin_order_message"));
    }

    if($('#admin_shop_message').data("admin_shop_message")){
        alertify.success($('#admin_shop_message').data("admin_shop_message"));
    }
});

function setId(id){
    $("#deleteuser_form").attr('action','/admin/delete_user/'+id);
    $("#deleteshop_form").attr('action','/admin/delete_shop/'+id);
    $("#delete_item_form").attr('action','/admin/delete_item/'+id);
    $("#delete_category_form").attr('action','/admin/delete_category/'+id);
    $("#deletecart_form").attr('action','/admin/delete_cart/'+id);
    $("#delete_order_form").attr('action','/admin/delete_order/'+id);
}

 


