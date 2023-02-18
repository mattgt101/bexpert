function maskasread(idx) {
    console.log(idx);
            $.ajax({
              type: "POST",
              url: '/trade/notification/read',
              data: {id: idx},
              success: function(){
                  location.reload();
              } 
            });
        }