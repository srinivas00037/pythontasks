#       *
#      * *
#     * * *
#    * * * *
#   * * * * * 
rows=5
for i in range(1,rows+1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)



#         *
#       * *
#     * * *
#   * * * *
# * * * * *
rows=5
for i in range(1,rows+1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "+" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)

# * * * * *
#  * * * *
#   * * *
#    * *
#     *

    rows=5
for i in range(rows,0,-1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

rows=5
for i in range(rows,0,-1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "+" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)

#     *
#    * *
#   *   *
#  *     *
# * * * * *

rows=5
for i in range(1,rows+1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        if i==1 or j==1 or i==rows or i==j:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)



#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


    rows=5
for i in range(1,rows+1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)

for i in range(rows-1,0,-1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)

# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

rows=5
for i in range(rows,0,-1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)
for i in range(2,rows+1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)