$("form#register").submit(function(e) {
    e.preventDefault();    
    var formData = new FormData(this);
    $.ajax({
        url: 'trade/includes/register.php',
        type: 'POST',
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        beforeSend:function(){
            $("#errorshow").hide();
		    $('#btnReg').html("<i class='fa fa-spinner fa-spin'></i> Creating Account...").attr("disabled", true);
		},
        success: function (data) {
			if (data == "OK") {
                $('#btnReg').html("<i class='fa fa-spinner fa-spin'></i> Account Created. Redirecting To Login").attr("disabled", false);
                $('#errorshow').addClass('alert alert-success');
				$("#errorshow").fadeIn();
                $("#errorshow").html("<i class='fa fa-spinner fa-spin'></i> Account Created. Redirecting To Login");

				window.location.href = "login";
			} else {
                $('#btnReg').html("Create Account").attr("disabled", false);
                $('#errorshow').addClass('alert alert-danger');
				$("#errorshow").fadeIn();
                $("#errorshow").html(data);
                document.getElementById("errorDisplay").scrollIntoView(true);
			}   
        },     
        error:function(){
			$('#btnReg').html("Create Account").attr("disabled", false);
			alert("Please check your internet connection");
		}
    });
});

function viewPassword(){
    var password = document.getElementById('password');
    var conPass = document.getElementById('confirm_password');
    if (password.type == 'password') {
        password.type = 'text';
        conPass.type = 'text';
        $('#passText').html("Hide Password <i class='fa fa-eye' aria-hidden='true'></i>");
    } else {
        password.type = 'password';
        conPass.type = 'password';
        $('#passText').html("Show Password <i class='fa fa-eye-slash' aria-hidden='true'></i>");
    }
}

$('#passText').click(function(){
    viewPassword();
});