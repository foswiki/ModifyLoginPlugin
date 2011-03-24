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
# **PERL**
# Modify the user based on the path<br />
# This is a hash table that maps a path in the format /web/topic
# to a username. The format is given as a perl hash definition<br />
# {<br />
# &nbsp;&nbsp;'/Myweb/TableAttributeSort' => 'calibration',<br />
# &nbsp;&nbsp;'/Database/Lookup' => 'DataBaseUser',<br />
# };
$Foswiki::cfg{Plugins}{ModifyLoginPlugin}{MapPathToUser} = {
};