#!/usr/bin/env python
import sys
import datetime

def get_lectures(fname):
    fh = open(fname, 'r')
    lectures = []
    for line in fh:
        f = line.rstrip('\n').split(';')
        if len(f) != 4:
            print(line, " does not have exactly 4 fields")
            sys.exit(1)

        l = {'lec':f[0], 'note':f[1], 'prepare':f[2],'bonus':f[3]}
        lectures.append(l)
    return lectures

def get_special_dates(fname):
    fh = open(fname, 'r')
    dates = []
    for line in fh:
        f = line.rstrip('\n').split(';')
        if len(f) != 3:
            print(line, " special dates should have exactly 3 fields (date, have-regular-class, info)")
            sys.exit(1)
        (month, day)= f[0].split('/')
        l = {'month':month, 'day':day, 'regular':f[1], 'lec':"<font color=\"red\">"+f[2]+"</font>"}
        dates.append(l)
    return dates

def is_special(special_dates, d):
    for sd in special_dates:
        if d.month == int(sd['month']) and d.day == int(sd['day']):
            return sd
    return None

def get_lab_due_dates(fname):
    fh = open(fname, 'r')
    dates = []
    for line in fh:
        f = line.rstrip('\n').split(';')
        if len(f) != 2:
            print(line, " lab due dates should have exactly 2 fields (date, lab assignment)")
            sys.exit(1)
        (month, day)= f[0].split('/')
        l = {'month':month, 'day':day, 'lab':f[1]}
        dates.append(l)
    return dates

def output_header():
    line = """
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no, content=no-cache">

	<!-- Bootstrap CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">

  <title>Computer Systems Organization (Fall 2019) </title>
</head>

<body>
<br>
    <main role="main" class="container">
      <header class="header clearfix">
        <nav>
          <ul class="nav nav-pills float-left">
            <li class="nav-item">
              <a class="nav-link" href="index.html">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link active" href="schedule.html">Schedule</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="labs">Lab</a>
            </li>
          </ul>
        </nav>
	<div class="row">
		<div class="col-sm-3"><img src="org2.png" width=150></div>
		<div class="col-sm-9">
		<div class="row">
        <h3 class="text-success">Computer Systems Organization</h3>
		</div>
		<div class="row">
			CSCI-UA.0201(007), Fall 2019
		</div>
		</div>
	</div>
      </header>

<div id="content">
<hr>
"""

    print(line)
    return

def output_footer():
    line = """
    </main>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.min.js" integrity="sha384-a5N7Y/aK3qNeh15eJKGWxsqtnX/wWdSZSKp+81YjTmS15nvnvxKHuzaWwXHDli+4" crossorigin="anonymous"></script>
</body>
</html>
"""
    print(line)
    return

if __name__ == '__main__':

    output_header()
    lecture_fname = "lectures.txt"
    special_fname = "special-dates.txt"
    lab_fname = "lab-dates.txt"
    if len(sys.argv) > 1:
        lecture_fname = sys.argv[1]
    if len(sys.argv) > 2:
        special_fname= sys.argv[2]
    if len(sys.argv) > 3:
        lab_fname= sys.argv[3]

    lectures = get_lectures(lecture_fname)
    special_dates = get_special_dates(special_fname)
    lab_due_dates = get_lab_due_dates(lab_fname)

    semester_start = datetime.date(2019,9,2) # enter first day of semester
    semester_end = datetime.date(2019,12,18)
    lec_day0 = 0 # enter lecture day of week
    lec_day1 = 2 # enter lecture day of week
    recitation_start = datetime.date(2019,9,5)
    recitation_end = datetime.date(2019,12,13)
    rec_day0 = 1 # enter recitation day of week

    line = """
<div class=\"row\">
<div class=\"col-sm-2\"><b>Date</b></div> 
<div class=\"col-sm-4\"><b>Lecture</b></div> 
<div class=\"col-sm-2\"><b>Reading</b></div> 
<div class=\"col-sm-2\"><b>Lab Due</b></div>
<div class=\"col-sm-2\"><b>Bonus Reading</b></div>
"""
    print(line)
    which = 0
    recitation = 1
    flip = 1 # flip background color for alternating week
    d = semester_start
    while d <= semester_end:

        if d.weekday() == 0 or d == semester_start: # start of the week, print container
            if flip == 0:
                print("<div class=\"container bg-light\">\n")
            else:
                print("<div class=\"container bg-white\">\n")
            flip = 1-flip

        prepare =""
        note = ""
        recitationStr = ""
        lec = ""
        labinfo= ""
        bonus=""

        specialLec = is_special(special_dates, d)
        labDue = is_special(lab_due_dates, d)
        if labDue is not None:
            labinfo = labDue['lab'] + " " + str(d.month) + "/" + str(d.day)

        # classes are on Monday and Wed
        if d.weekday() == lec_day0 or d.weekday() == lec_day1:
            if specialLec is None:
                l = lectures[which]
                which=which+1
                lec = l['lec']
                note = l['note']
                prepare=l['prepare']
                bonus=l['bonus']
            else:
                lec = specialLec['lec']
        elif specialLec is not None and specialLec['regular'] == "1":
            l = lectures[which]
            which = which+1
            lec = specialLec['lec']+"<br>"+l['lec']
            note = l['note']
            prepare=l['prepare']

        if lec != "":
            print("<div class=\"row\">")
            print("   <div class=\"col-sm-2\">%d/%d</div>" % (d.month, d.day))
            print("   <div class=\"col-sm-4\">%s " % (lec))
            if note != "":
                print("  [<a href=\"notes/%s\">note</a>]</div>" % (note))
            else:
                print("</div>\n")
            print("   <div class=\"col-sm-2\">%s</div>" % (prepare))
            print("   <div class=\"col-sm-2\">%s</div>"  % (labinfo))
            print("   <div class=\"col-sm-2\">%s</div>"  % (bonus))
            print("</div>\n")

        # Deal with recitations  on thu
        if d.weekday() == rec_day0 and d >= recitation_start and d <= recitation_end:
            print("<div class=\"row\">")
            print("   <div class=\"col-sm-2\">%d/%d</div>" % (d.month, d.day))
            if specialLec is None:
                print("   <div class=\"col-sm-4\"><a href=\"https://github.com/nyu-cso-sp19/cso19-recitations/tree/slides/r%02d/r%02d.pdf\"><em>recitation%02d</em></a></div>" % (recitation, recitation, recitation))
                print("   <div class=\"col-sm-2\"><em></em></div> ")
                recitation = recitation + 1
            else:
                print("   <div class=\"col-sm-2\">%s</div> " % specialLec['lec'])
                print("   <div class=\"col-sm-2\"></div> ")
            print("   <div class=\"col-sm-2\">%s</div>"  % (labinfo))
            print("   <div class=\"col-sm-2\">%s</div>"  % (bonus))
            print("</div>\n")
        if d.weekday() == 6: # terminate week container on Sunday
            print("</div> <!--dark/light-->\n")

        d = d + datetime.timedelta(1) # go to next day

    if which != len(lectures):
            print("%d weeks total not equal to %d lectures planned" % (which, len(lectures)))
            sys.exit(1)


    output_footer()
