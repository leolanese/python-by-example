# demonstrate template string functions
from string import Template

def main():
    # 1
    # Usual string formatting with format()
    str1 = "Template string functions: {0} - {1} - {2}".format("Hello", "World", "!")
    print('1 - ' + str1)

    # 2
    # create a template with placeholders
    templ = Template('Template with placeholders: ${v1} - ${v2} - ${v3}')
    # use the substitute method with keyword arguments
    str2 = templ.substitute(v1="Hello", v2="World", v3='!')
    print('2 - ' + str2)
    
    # 3
    # use the substitute method with a dictionary
    data = { 
        'v1': 'Hello',
        'v2': 'World',
        'v3': '!'
    }
    str3 = templ.substitute(data)    
    print('3 - ' + str3)
    
if __name__ == "__main__":
    main()
    
# 1 - Template string functions: Hello - World - !
# 2 - Template with placeholders: Hello - World - !
# 3 - Template with placeholders: Hello - World - !    
