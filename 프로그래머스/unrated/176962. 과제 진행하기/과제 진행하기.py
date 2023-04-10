import datetime as dt


def solution(plans):
    studies = parsing(plans)
    ans = []
    st = []

    prev_subject, prev_starttime, prev_taketime = studies[0]
    prev_end = prev_starttime + prev_taketime

    for current in studies[1:]:
        if prev_end > current[1]:
            st.append([prev_subject, prev_taketime - (current[1] - prev_starttime)])
        else:
            ans.append(prev_subject)
            left = current[1] - prev_end
            while st:
                if st[-1][1] > left:
                    st[-1][1] -= left
                    break
                else:
                    left -= st[-1][1]
                    ans.append(st[-1][0])
                    st.pop()

        prev_subject, prev_starttime, prev_taketime = current
        prev_end = prev_starttime + prev_taketime

    ans.append(prev_subject)
    while st:
        ans.append(st.pop()[0])

    return ans


def parsing(plans):
    datas = []
    for plan in plans:
        subject = plan[0]
        start_time = dt.datetime.strptime(plan[1], '%H:%M')
        start_time = 60 * start_time.hour + start_time.minute

        taken_time = int(plan[2])
        datas.append([subject, start_time, taken_time])

    datas.sort(key=lambda t: t[1])
    return datas
