
#################################################
## Consts
#################################################

URL="https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observation_LJUBL-ANA_BEZIGRAD_latest.xml"
XML_FILE="output.xml"

#################################################

wget \
    -O $XML_FILE \
    $URL
