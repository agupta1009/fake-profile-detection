<html>

<body bgcolor=#a3cfb4>

    <center>

        <h1>  PREDICTION :  </h1>
    
    {%if data == 0%}
    <h1>Iris-setosa</h1>  
    <img src='static\setosa.jpg'>  

    {%else%}
    <h1>Iris-versicolor</h1>
    <img src='static\verci.jpg'>
    
    {%endif%}

        <br><br>
    <a href='/'>go back to home page</a>

    </center>

</body>

</html>