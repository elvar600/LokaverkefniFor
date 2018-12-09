% rebase("base.tpl", title="Skráningarform")

	<link rel="stylesheet" type="text/css" href="\static\text.css">
	<link rel="stylesheet" type="text/css" href="\static\css.css">



<p>Rithöfundur: <b>{{u}}</b></p>

<form  action="about" accept-charset="ISO-8859-1">
	<h2>News</h2>
	<h3>Titil</h3>

	<h4>
		<label><input type="title" name="titil" ></label>
		
	</h4>
	<h4>
		<label><textarea name="text">type in news</textarea></label>
	</h4>


	<input type="submit" name="Skráning">
	<input type="reset" name="Hreinsa">
</form>


	

</form>