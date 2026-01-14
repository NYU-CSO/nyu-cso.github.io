import sys
import datetime

semester_start = datetime.date(2026,1,20) # enter first day of semester
semester_end = datetime.date(2026,5,8)
lec_day0 = 0 # enter lecture day of week (Mon)
lec_day1 = 2 # enter lecture day of week (Wed)

recitation_start = datetime.date(2026,1,23)
recitation_end = datetime.date(2026,5,5)
rec_day0 = 4 # enter recitation day of week

def get_lectures(fname):
    fh = open(fname, 'r')
    lectures = []
    for line in fh:
        f = line.rstrip('\n').split(';')
        if len(f) < 3:
            print(line, " does not have exactly 4 fields")
            sys.exit(1)
        l = {}
        l['lec'] = f[0]
        l['note'] = f[1]
        l['prepare'] = f[2]
        if len(f) >=4: 
            l['bonus']=f[3]
        else:
            l['bonus']=' '
        lectures.append(l)
    return lectures

def get_special_dates(fname):
    fh = open(fname, 'r')
    dates = []
    for line in fh:
        if line.startswith('#'):
            continue
        f = line.rstrip('\n').split(';')
        if len(f) != 3:
            print(line, " special dates should have exactly 3 fields (date, have-regular-class, info)")
            sys.exit(1)
        (month, day)= f[0].split('/')
        l = {'month':month, 'day':day, 'classday':int(f[1]), 'description':"<font color=\"red\">"+f[2]+"</font>"}
        dates.append(l)
    return dates

def is_special(special_dates, d):
    for sd in special_dates:
        if d.month == int(sd['month']) and d.day == int(sd['day']):
            return sd
    return None

def is_lecture_day(day):
    if day == lec_day0 or day == lec_day1:
        return True
    return False

def is_recitation_day(day):
    if day == rec_day0:
        return True
    return False

def get_lab_due_dates(fname):
    fh = open(fname, 'r')
    dates = []
    for line in fh:
        if line.startswith('#'):
            continue
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
        <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no, content=no-cache">

	<!-- Bootstrap CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">

  <title>Computer Systems Organization (Spring 2026) </title>
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
        <h3>Computer Systems Organization</h3>
		</div>
		<div class="row">
			CSCI-UA.0201(007), Fall 2026
		</div>
		</div>
	</div>
      </header>

<div id="content">
<hr>
<div class="row">
    <ul> 
      <li>[KR] refers to Kernighan/Richie's book.
      <li>[BO] refers to Bryant/O'Hallaron's book.
      <li>[PH] refers to Patterson/Henessy's book.
    </ul>
</div>
<hr>
<div class="row"></div>
"""

    print(line)
    return

def output_footer():
    line = """
    </main>
    <hr>
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

    line = """
<div class=\"row\">
   <div class=\"col-sm-2\"><b>Date</b></div> 
   <div class=\"col-sm-4\"><b>Lecture</b></div> 
   <div class=\"col-sm-4\"><b>Reading</b></div> 
</div>
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

        specialLec = is_special(special_dates, d)

        #skip no class dates
        #if (specialLec != None and specialLec['classday'] < 0) or (specialLec is None and is_lecture_day(d.weekday()) is False and is_recitation_day(d.weekday()) is False):
        if specialLec is None and is_lecture_day(d.weekday()) is False and is_recitation_day(d.weekday()) is False:
            d = d + datetime.timedelta(1) # go to next day
            if d.weekday() == 6: # terminate week container on Sunday
                print("</div> <!--dark/light-->\n")
            continue

        print("<div class=\"row\">")
        weekday_str = d.strftime("%a")
        print(f'   <div class=\"col-sm-2\">{d.month}/{d.day} <span style="color:#888; font-size:0.85em;">{weekday_str}</span></div>')

        if (specialLec is not None and is_lecture_day(specialLec['classday'])) or (specialLec is None and is_lecture_day(d.weekday())):
            try:
                l = lectures[which]
                print("   <div class=\"col-sm-4\">", end=" ")
                if specialLec is not None:
                    print(f'{specialLec["description"]}<br>', end=" ") 
                print(l['lec'], end=" ")
                if l.get('note') == '':
                    print("  </div>")
                else:
                    print("  [<a href=\"notes/%s\">note</a>]</div>" % (l.get('note')))
                print("   <div class=\"col-sm-4\">%s</div>" % (l.get('prepare')))
            except IndexError as e:
                print(f"IndexError: {e}")

            which = which+1
        elif (specialLec is not None and is_recitation_day(specialLec['classday'])) or (specialLec is None and is_recitation_day(d.weekday())):
            print("   <div class=\"col-sm-4\"> ", end="")
            if specialLec is not None:
                print("%s<br>" % (specialLec['description']), end="")
            print("<a href=\"rec-notes/r%02d.pdf\"><em>recitation%02d</em></a></div>" % (recitation, recitation), end="") 
            print("   <div class=\"col-sm-4\"></div>") # empty prepare for recitation
            recitation = recitation + 1
        elif specialLec is not None and specialLec['classday'] < 0:
            print(f'   <div class=\"col-sm-4\">{specialLec["description"]}</div>', end=" ")
            print("   <div class=\"col-sm-4\"></div>")
        elif specialLec is not None and specialLec['classday'] >=0:
            assert False
 
#        labDue = is_special(lab_due_dates, d)
#        if labDue != None:
#            print("   <div class=\"col-sm-2\">%s</div>"  % (labDue.get('lab')))
#        else:
#            print("   <div class=\"col-sm-2\"></div>")
#            
        print("</div>\n")

        d = d + datetime.timedelta(1) 

    if which != len(lectures):
            print("%d lectures total not equal to %d lectures planned" % (which, len(lectures)))
            sys.exit(1)


    output_footer()
