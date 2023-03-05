#! /usr/bin/env perl

use strict;
use warnings;
use utf8;
use CGI;
use Encode;

my $q = CGI->new;
my $method = $q->request_method;
my $url = $q->self_url;
my $script = $q->script_name;
my $query = $q->query_string;


print $q->header(
    -type => 'text/html',
    -expires => 'now',
    );
print <<EOF
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>results</title>
    </head>
    <body>
        <table>
            <thead>
                <tr>
                    <th>name</th>
                    <th>value</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>method</td>
                    <td>$method</td>
                </tr>
                <tr>
                    <td>URL</td>
                    <td>$url</td>
                </tr>
                <tr>
                    <td>query</td>
                    <td>$query</td>
                </tr>
            </tbody>
        </table>
        <form method="POST" action="$script">
            <input name="text" type="text"/>
            <button>submit</button>
        </form>
    </body>
</html>
EOF
