def translate_text(target, text):
    return 'The residential complex "Rusanivska Gavan" is part of the development of a new microdistrict: new residential complexes with their own shopping infrastructure, two kindergartens and a school will be built on the site of an abandoned industrial zone. Only two houses belong to "Rusanivska Havana" - one on the first line and one more on the second. Combined, both buildings will be a common residential area, where there will be underground parking, and on its roof - a closed courtyard without cars. The main idea of ​​the "Rusanivska Gavan" complex is the advantages of living near the water: views of the Dnipro and Trukhanov Island, as well as an equipped embankment along the shore. Infrastructure You can reach the city train station in 10 minutes from the complex, and after the completion of the construction of the Podilsk bridge crossing and the Podilsk-Vygurivska subway line, it will be even more convenient to get to the right bank. There are supermarkets of large retail chains nearby: 15 minutes on foot to Novus and " Silpo", 10 minutes by car to Varus, another Novus and another "Silpo". You can also reach the Left Bank market in 5 minutes, where fresh fruits and vegetables are sold. As part of the development of the new neighborhood, 2 kindergartens and 1 school will be built, which will make it easier for young families to find a preschool. If suddenly there are not enough places or something doesn\'t work out, there are other kindergartens in the area nearby: 15 minutes on foot to #566, 8 minutes by car to Kraina Dytynstva, 10 minutes by car to kindergartens #337, #261 and #444. For older children, schools #72, #65, #128 and Ukrainian College named after V.O. Sukhomlynskyi. To train nearby, you will need to walk for 15-20 minutes or drive 5-7 minutes to the fitness clubs "Sport Land", the Iron fitness club, the Grand Sport and "Atletico-fitness" clubs. 7 minutes by car - and you are in A hydropark, where you can sunbathe on the beach, take a walk in the fresh air, ride a bike, sit in a cafe or take your child to attractions. Features include its own boiler room for each house, an equipped embankment on the banks of the Dnipro — a place for walks, morning jogs and relaxing on sunbeds, a sports area with exercise machines sky, children\'s play areas for children of all ages'

    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    return result['translatedText']

    # print(u"Text: {}".format(result["input"]))
    # print(u"Translation: {}".format(result["translatedText"]))
    # print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
