jQuery(document).ready(function() {
                $value = $("#question").val();


        $("#submit-button").click(function(e) {
          e.preventDefault();


          $.ajax({
              type: "POST",
              url: "/chatbot",
              data: {
                 question: $("#question").val()

              },
              success: function(result) {



               $value = $("#question").val();

               $msg = '<div class="user-inbox inbox"><div class="msg-header"><p>'+$value+'</p></div></div>';
               $(".form").append($msg)

                  if(result.hasOwnProperty("greetings")){

                                           $rpymsg = '<div class="bot-inbox inbox"><div class="icon"><i class="fas fa-user"></i></div><div class="msg-header"><p>'+result.greetings+'</p></div></div>';

                  }
                  else if(result.hasOwnProperty("names")){
                      $rpymsg = '<div class="bot-inbox inbox"><div class="icon"><i class="fas fa-user"></i></div><div class="msg-header"><p>'+result.names+'</p></div></div>';


                  }
                  else if(result.hasOwnProperty("bye")){
                      $rpymsg = '<div class="bot-inbox inbox"><div class="icon"><i class="fas fa-user"></i></div><div class="msg-header"><p>'+result.bye+'</p></div></div>';


                  }
                  else if(result.hasOwnProperty("link")){
                      $rpymsg = '<div class="bot-inbox inbox"><div class="icon"><i class="fas fa-user"></i></div><div class="msg-header"><p>'+result.link+'</p></div></div>';


                  }
                  else if(result.hasOwnProperty("thanks")){
                      $rpymsg = '<div class="bot-inbox inbox"><div class="icon"><i class="fas fa-user"></i></div><div class="msg-header"><p>'+result.thanks+'</p></div></div>';


                  }
                  else if (parseFloat(result.answer[0].score) <= 0.5) {
                      console.log(result.answer[0].score)
                      $rpymsg = '<div class="bot-inbox inbox"><div class="icon"><i class="fas fa-user"></i></div><div class="msg-header"><p>I cant understand this question</p></div></div>'
                  }
                  else {
                      $rpymsg = '<div class="bot-inbox inbox"><div class="icon"><i class="fas fa-user"></i></div><div class="msg-header"><p>' + result.answer[0].answer + "<br>Text context:" + result.answer[0].text + '</p></div></div>';
                      $rpymsg2 = '<div class="bot-inbox inbox"><div class="icon"><i class="fas fa-user"></i></div><div class="msg-header"><p>' + result.answer[1].answer + "<br>Text context:<br>" + result.answer[1].text + '</p></div></div>';
                            console.log(result.answer[0].score)
                  }
               $(".form").append($rpymsg);

               $(".form").scrollTop($(".form")[0].scrollHeight);

                $("#question").val("");
              },
              error: function(result) {
                  alert('error');
              }
          });



        });

      });