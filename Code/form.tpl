<html>
  <head>
      <title>Amrita Tamil Paraphrase</title>
  </head>
  <body>
  <style>
body  {
    
}
.button {
    background-color: dodgerblue;
    border: none;
    color: yellow;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    -webkit-transition-duration: 0.4s; /* Safari */
    transition-duration: 0.4s;
}
.button1:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
}


header, footer {
    padding: 0.1em;
    color: blue;
    background-color: skyblue;
    clear: left;
    text-align: center;
}
label, label>input{
    font-size: 20px;
    display: inline-block;
    margin: 0;
    line-height: 18px;
    height: 28px;
    vertical-align: top;
}
</style>
<header>
<h1>Center for Computational Engineering and Networking (CEN)</h1>
   <h2>TAMIL PARAPHRASE</h2>
</header>
    <form method="post" action="/">
        <fieldset>
            <legend>Center for Tamil Natural Language Processing Research & Amrita NLP Group</legend>
            <ul>
               <div style="text-align:center"> 
        <TEXTAREA style="color:purple; resize:none; font-size: 12pt" id="myTextarea" NAME="first" ROWS="5" cols="50" placeholder="Enter the first sentence here....."></TEXTAREA>
<TEXTAREA style="color:purple; resize:none; font-size: 12pt" id="myTextarea1" NAME="last" ROWS="5" cols="50" placeholder="Enter the second sentence here....."></TEXTAREA>
</div>
<br>
				<br>

				<fieldset>
	<legend>Select Your Option:</legend>
	<div style="text-align:center"> 
	<label for="radChoiceGood">DTM
		<input type="radio" id="DTM" name="radioButton" value="DTM">
	</label>
	
	<label for="radChoiceExcellent">TFIDF
		<input type="radio" id="TFIDF" name="radioButton" value="TFIDF">
	</label>
	</div>
</fieldset>

            </ul><div style="text-align:center"> 
        <button id="myButton" class="button button1" >Check</button>
        </div> 				
			
        </fieldset>
    </form>
    </script>
<script type="text/javascript">
    document.getElementById("myButton").onclick = function () {
        var s1 = document.getElementById("myTextarea").value;
        var s2 = document.getElementById("myTextarea1").value;
var val = '';
if(document.getElementById('DTM').checked) {
  val = document.getElementById('DTM').value;
}else if(document.getElementById('TFIDF').checked) {
  val = document.getElementById('TFIDF').value;
}
        if (s1 == "") {
        alert("Enter the sentence for first Text box");
        return false;
    }
    else if (s2 == "") {
        alert("Enter the sentence for second Text box");
        return false;
    }
     else if (val == "") {
        alert("Select any one radio button");
        return false;
    }
    };
  
</script>
    
	<div align="center">

	
<p style="color:brown;"><span style="color:DarkViolet ;font-weight: bold;font-size:18px">First Sentence:</span> {{info}}</p>
<p style="color:MidnightBlue ;"><span style="color: Indigo ;font-weight: bold;font-size:18px">Second Sentence:</span> {{inf}}</p>
<p style="color:blue;"><span style="color: MidnightBlue ;font-weight: bold;font-size:18px">Result:</span> {{st}}</p>
<p style="color:DarkBlue;"><span style="color: DarkGreen;font-weight: bold;font-size:18px">Similarity Score:</span> {{stm}}</p>
		 </div>

<footer> <a href="http://nlp.amrita.edu/">Amrita NLP Group</a> </footer>		 
  </body>
</html>
   
