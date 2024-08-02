odoo.define("custom_website.WebsiteFormValidation", function(require){
'use strict';
var publicWidget = require("web.public.widget");
        console.log('clicked');

publicWidget.registry.WebsiteFormValidation = publicWidget.Widget.extend({
    selector:"#res_partner_creation",
    events:{
        'submit': "_onSubmitButton",

    },
    _onSubmitButton: function(evt){

        var resName = this.$("input[name='name']").val();
        var resEmail = this.$("input[name='email']").val();
        var resPhone = this.$("input[name='phone']").val();
        var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        var phonePattern = /^\d{10}$/;
        var checkingEmail = emailPattern.test(resEmail);
        var checkingPhone = phonePattern.test(resPhone);
        $("#client_side_validation").hide();
        if(!resName){
            $("#client_side_validation").html("Please enter name.");
            $("#client_side_validation").show();
            evt.preventDefault()
        }

        else if(!resEmail){
            $("#client_side_validation").html("Please enter email.");
            $("#client_side_validation").show();
            evt.preventDefault()
        }
        else if(!checkingEmail){
            $("#client_side_validation").html("Enter valid email.");
            $("#client_side_validation").show();
            evt.preventDefault()
        }

        else if(!resPhone){
            $("#client_side_validation").html("Enter phone number.");
            $("#client_side_validation").show();
            evt.preventDefault()
        }
        else if(!checkingPhone){
            $("#client_side_validation").html("Enter valid phone number.");
            $("#client_side_validation").show();
            evt.preventDefault()
        }


    }

})
})