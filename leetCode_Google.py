def numUniqueEmails( emails):
    # Separate doemain name from the each emails after "@"
    # Then work with local name if it has "+" it would be ignoring everything after that
    # When it has "." it would concatonate

    email_separation = {} #emial_separation = {email: [local_name, domain_name]}
    uniqueEmails = set()

    for email in emails:
        email_local_index = email.find("@")
        email_local_name = email[:email_local_index]
        email_domain_name = email[email_local_index:]



        email_separation[email] = [email_local_name, email_domain_name]
        proces_email = email_local_name.replace('.','')
        plus_finder = proces_email.find('+')


        if plus_finder != -1:
            proces_email = proces_email[:plus_finder]


        fullyprocessed_email = proces_email + email_domain_name

        uniqueEmails.add(fullyprocessed_email)
        # print(email_separation)

    return uniqueEmails






emails1 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
emails2 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails1))

print(numUniqueEmails(emails2))