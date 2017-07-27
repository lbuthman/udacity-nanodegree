#!/usr/bin/env python2.7

from clint.textui import puts, indent, prompt


def welcome_screen():
    puts("==========================================================================================================\n"
         "==========================================================================================================\n"
         " @@   ##     ##   ####  ###   ##  ######  #######   @^@   #######   ###    ###   ##  #######  ######   @@\n"
         " @@   ###   ###  ##  ##  #    #     ##    ##        @^@   ##       ## ##    #    #   ##       ##       @@\n"
         " @@   ## # # ##  ##  ##   #  #      ##    ####      @^@   ####    ## # ##    #  #    ####       ##     @@\n"
         " @@   ##  #  ##  ##  ##    ##       ##    ##        @^@   ##      ##   ##     ##     ##          ##    @@\n"
         " @@   ##  #  ##   ####     ##     ######  #######   @^@   ##      ##   ##     ##     #######  ######   @@\n"
         "==========================================================================================================\n"
         "==========================================================================================================\n"
         "***                                                                                                   ***\n"
         "***       Hello and welcome to the infamous Movie Faves website generator, courtesy of Udacity        ***\n"
         "***       and me, Luke Buthman! Creating spiffy movie websites is easy, just enter your favorite      ***\n"
         "***       movies below.                                                                               ***\n"
         "***                                                                                                   ***\n"
         "***       When you are done and ready to make your website, simply type q or quit. Your html          ***\n"
         "***       website will then be kneaded, tossed, and baked in no time. Have fun! Impress your          ***\n"
         "***       friends! Rule the world!                                                                    ***\n"
         "***                                                                                                   ***\n"
         "*********************************************************************************************************\n"
         "\n")


def get_movie(input_number):
    query_string = "Enter your #" + str(input_number) + " favorite movie: "
    with indent(4, quote=' >'):
        return prompt.query(query_string)
