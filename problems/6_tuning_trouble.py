import pytest

def get_marker(input):
    marker_length = 4
    for i in range(len(input) - marker_length + 1):
        marker = input[i:(i+marker_length)]
        unique_characters = set(marker)
        if len(unique_characters) == marker_length:
            return i + marker_length

def test_get_marker():
    assert(get_marker('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5)
    assert(get_marker('nppdvjthqldpwncqszvftbrmjlhg') == 6)
    assert(get_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10)
    assert(get_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11)


if __name__ == '__main__':
    input = 'srlsrsnnwhwwmddwfddgldlglppcnpptftzzchzhbhmmvwmvwvvjsjnjbbvbmvmnmqmfmjfjjmllzddrvrrnsncnznndwwqrqjjsfsjsjsvsvzvtvfvrvhhbwwltttbhhvphhtqqnffsppdqqrmmfrmfrrwvrvrsvrsrzssrqqrfqrfrttqntnpttvrrcncnfftjfjwwfwjwpwwltlwwwvnvcnvvdgvddqlddnllrggqvgvzzjddfgdfdgfffsbfsffjmffprrmgmtmqqgzzlwldlbbgjjnfjnnvlnnlbbnjnzngglmggwtgwttnvtnvndndmnmdmcddzbdbbspbpwbpplvpvnnmtmqqwnwgglhghdhbhqbhhqrqhqcqmmmrwwlvvfnvfnnpddbfbgfgqglgddrggbgbqqfwfjfdjfflzldlbbsbbtftccgqggzgdglglzljjzbzfbzffgftfvtfvvvjmjzjmjfjqqccpcjppzfpzzsvvzjvvfgfmgffzhhdphdpdwdwmdwwlqljjzffzvfzfwzfzcztctssdpssndssvbbtbstbtnngjjspplttpffjggbbqsqnqcncscpcmccbmbdbtbcbbgqgwgwqgwgwsszqznzvvntvvmlvlvqqvgvwgwlldbblclqcqggtqqlsqlsqlqcczzqgghmgmrgmrggljlbjbsbsmmnlmmdppnpfnnvhnnzggchgggbwwvtvpptgpplsljjshhnphhblbnbpbgppfllhsllbtlbtllrprqrvvfgvgpgcpcdddjjplpssjrjqjggncnzccqdqfqpffvddhlhdllgzzrtrztrztzptztwwbjbnjnsjsfsbfbdbccnhnmhnhrhwhfhbbtzbtztzrttrzrfrcrtctqqrlrsshphwphwpwwcmczzpqzqztqqvzzshhddrvdrrztrrqcqbcqbbhnnpfnpfnnmcnmnccnmmhccjjwzwcwbwcwnngtnngrngnsnzzcvvvtnvvtpvtpvtvvhffbsfsnsdsmmzbbrqbqpbpcpdppzmzbmmtdmttvgvrvlrvvhddjgdjdbbthtjhjdjhdjjmssdldjllwppvbvnbnlbbbszbblpbpfbpblbzzszvssbcbgcghgbbcpbbqrrdjdnnjcjddjcdjjcqqhggflftftfhttvlttgdtdrttwppwvvrzzbggrjjmssrjsjmssdtttdbdvddpllpgllthhvfvhvddrhhnznwznwzzpbblvvpmvpmpddjvdvcddvsshfhrrghgnhghmhhmhffrsfrflrfrjrddzgzsggchcfhhsbbsrszzgjggnrrgfffhthdthtnhtntllsjjjwqqsbsttbtzbttlfttczzbfbwfwvvhllltjjsqsdqqspqsszqzhhdrrhccgbcgggcbggnvgvmmwcmmpqmqccshsnnnwrwfrrwrllvhvlvmlvljjgrgvrvddfqfwqfqlfqqqppvmvrmrfrvrwrqrjqrrvmrvmrrvffmtffsfdfdrdwrwjrrcgcwwcdwdrdnrnzztqzzzgdzgdgldltdtvtnnhllrtltbtrbbttgssdhsssrmsscnssmtmqqtssmzzjqzqddfrdrtdrdpdzzppwggsrrfvfnvvmgvgmmdnnbwnntlnntncchcmcjmmvzzzngznnbgbnbnvbvzzfqqmtmrmcmqmvmbmbmcmscsjcsshswsjsvswshwwlnnsslmslmmzgmgsmssrwwmjwmwllvbvppplmmwgmgzgzdgzdgzztrtzzchcssbppdbbmvmqmmzhztzdtzdznnqhhmcmnnncbnngjnjmjnmmqqsnqsnslnlqlppvbvwwvtwtfwtfmzsbdjfvhzcflstpbtprpzmwcwwgzshfssnjdgflcsfglhbvvdctfrccfmwgfvjtvqfqpzzmqtlbvrjqwlwclfzhfzcmwsvprdhzcrghdscprrnqgdgmhhwbcfcfzrcgrwvbstpwbcvcnpmftwwthnsjznzslfdfqhtpsgmjsddmhlhtlzfsnhlcbgnqpqbzppnbcgtzvwdpmgftgsmrwjqwsdnjrrmwrmlcvlqgwldnvmsgnwccwzmdzwdhpmpqffgbnrrrvzqhtlnvqfhgwbbwsghwbrjzjcjmjmsspcmnfbbpmwffbdqffqfwsvtcrghbnldspdhjhjvtdhgmvrzqqlhvnwbdhfprwqdtzswfdzdwhzvfzsfqlzcflhbsvjhnjnthrdrgmjrrbftflpvrmrvvsgnjhrhjffvznmbjtshwgjmcqbfqjlptsrcgzvrhctwsdclrstmsbsbpqpjcvftmvmsmpwmmphlwmljhvllhrmfcncdprrwfmqrlllmsrvrwtbsqddbmblhvqqlcbbtjbslggrshflrddsphbvzhprcvbpmfldnmwtchddbdwhwpgbmjqptsbdzhrbqfwgfltchsggjlbqbhmzbjdncnvsqjvftpwrpdcjzsrvrlzwqfptwzssqpltjhdmtmmgvjzzqswwrsqrqfpdllgzsdlvhfdnzlrmlqdclwhqqbtwdqcrlfdjphjvcfzpwwgphmrldnwjpnmsjnqpwtwglcbthmcbnvpmjbdhmjglgccsmrmbvbqphdlbrrgnbljlhqvgqbctmthvmsfzflwvctwmdgmrlhnmwnsjtzndlwfttcvtslppjwsgbzhztlpzhmjlrbtzfnblwwlddzwqvzbjmffbflvmvnsgjlqwjqvrcrtwbhfzbzzmtwsndqmtnbjbsqjpnwhzqgwwltwgrqfbhjtpzrqvvhgjsbzqmfdsmzjdnplvblvqlrtzsbjgdptdhgvvrblbjppnnhhnvqtmjgwqzwtmjglrjlwsrfdjfmzlsszzzpbwvjbwpcwlplhcmhgpclztjcrmcntnqbnlrmcnhcnhnmjggtqbtvcfmcbdpqhdrvspbrgcwhgjhggwpvjbplhdsnnvgbzhmcrjqvqlwsdvrrnntmwdgdqdvzznjflctlfmfzsdfbpftsscnbtnqcsvtltvnsqpghzcwtjctvwqqnvnddlzbftwrdqzltpczrbmvsmlpfjzphtpnngzdfrjqrtbppbvztsddblspbltsnrtdftmwbblgdqvmscjqpwfvdzphwqgrbpdfcvtvmddgjjpswrqnwjfghtzwzbhtjnwjsrnwhjwcwnrtwrmbmqjhrbmbsslnvtsqnlbzlfdjvmnlhccpzmvpmrnttnshdjsswjlbtpwdwgmzqcthbczngwnfpzbmmrdffqsbrmsgzrtpsstfmdgbclwthflfbzvtptdfpzznvdwncqzvjwsmczwcnwgjpffcbhrtmtnbtjgcvtwdjtrftjwgvzmlfvgdjjjgsftzctplmjjmqfdzzwrtfmwqhwzglwbvsdvtgphsmngvppvlfdjdrzhhzsrvqgfwjbqdqlrwbgdmrglzrchvgwlhhwbvhfszntbrhshvqdznfvngdmhctjnlfhsmchqbqhdtmlntsnpvdzrvwjcjflfqgnprcpscfcmlgbwzmbnfdfnbwngrrbpnvbcdfgcpgtwmtbzptsdvjhwnzpsffglnqlczgsrdzshrfpqtqbmsrgzwwjvqhzjfzldcggvfhtcvzsgfspnlgtjfglwcnbprvssdfbtzqbblzjzmtftfcfprlwsvswjvtpzcpfphvmdnbczzjbjjrpwrncdszrtqjvznvgzcwdvpfvfcqlsdmhsswpnfsvtffnjhstcznwghlpmmqbnhqtddbjdrpvfhgdwjcnfgggmwnqhmsvgzsssbfcfrmbwpfqhrmtdvhbpwzggdvfjnlrgmvjjbqhjmbvszfzdcwrcjhfdczbhmcrwngmrgrldvbjjdgddhbbvqvwztfstfzqnqwvmmdzhzqtrmnqfrhmtdfhrgfqclpqdwthrbgsprccwcsvdbnclglgflhtqstvpwrmnsvflpplrgftlvjwttmdcqwjnbttjqqlwsntplmfrncqzplwgrjpzljtmnwsqfqnzgnrbtscbfzqwnqttnghcgl'
    print(get_marker(input))