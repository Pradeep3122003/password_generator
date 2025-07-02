#!/bin/bash

charset=""
length=8

for arg in "$@"; do
  case $arg in
    -n) charset+="0-9" ;;
    -a) charset+="a-z" ;;
    -A) charset+="A-Z" ;;
    -S) charset+="!@#$%^&*()_+=-{}[]:;<>,.?/" ;;
    [0-9]*) length=$arg ;;
  esac
done

if [ -z "$charset" ]; then
  charset="a-zA-Z0-9!@#$%^&*()_+=-{}[]:;<>,.?/"
fi

if [ "$length" -lt 5 ]; then
  < /dev/urandom tr -dc "$charset" | head -c "$length"
  echo
  exit 0
fi

build_password() {
  result=""
  [[ "$charset" == *"a-z"* ]] && result+=$(< /dev/urandom tr -dc 'a-z' | head -c1)
  [[ "$charset" == *"A-Z"* ]] && result+=$(< /dev/urandom tr -dc 'A-Z' | head -c1)
  [[ "$charset" == *"0-9"* ]] && result+=$(< /dev/urandom tr -dc '0-9' | head -c1)
  [[ "$charset" == *"!"* ]]   && result+=$(< /dev/urandom tr -dc '!@#$%^&*()_+=-{}[]:;<>,.?/' | head -c1)
  restlen=$((length - ${#result}))
  [[ $restlen -gt 0 ]] && result+=$(< /dev/urandom tr -dc "$charset" | head -c "$restlen")

  echo "$result" | fold -w1 | shuf | tr -d '\n'
  echo
}

build_password

#command issue while generating mixtures
