window.onload = function(){
                var Input = document.getElementById("myInput");
                var messageBox = document.getElementById("messageBox");
            
            function post(){
                if(Input.value){
                    var oTime = document.createElement("div");
				    oTime.className = "time";
				    var myDate = new  Date();
				    oTime.innerHTML = myDate.toLocaleString();
				    messageBox.appendChild(oTime);
				
                    var message = document.createElement("div");
                    message.className="messageX";
                    message.innerHTML=Input.value;
                    Input.value="";
                    messageBox.appendChild(message);
                }
            }
        }
