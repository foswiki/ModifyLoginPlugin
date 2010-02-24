# ---+ Extensions
# ---++ ModifyLoginPlugin
# **SELECT none,uppercase,lowercase**
# Change case of the login name.<br />
# none - no case change is done
# upper - the login name is changed to uppercase
# lower - the login name is changed to lowercase
$Foswiki::cfg{Plugins}{ModifyLoginPlugin}{ChangeCase} = 'none';
# **BOOLEAN**
# Strip all characters after a @ including the @ 
$Foswiki::cfg{Plugins}{ModifyLoginPlugin}{StripAfterAtsign} = 0;
