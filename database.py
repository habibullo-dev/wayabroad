import os
import boto3
import pymongo
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import json

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection = f"mongodb+srv://toby:{password}@wayabroad.ytg2mkg.mongodb.net/?retryWrites=true&w=majority&appName=wayabroad"

client = MongoClient(connection)

# Get a reference to the MongoDB collection
db = client['universityDB']  # replace 'your_database_name' with the name of your database

# Get a reference to the universities collection
universities_collection = db['majorsDB']


data = {
    "Ajou University": {
        "english_track": {
            "School of Business": [
                "Business Administration"
            ]
        },
        "korean_track": {
            "College of Engineering": [
                "Mechanical Engineering",
                "Industrial Engineering",
                "Chemical Engineering",
                "Material Science and Engineering Applied Chemistry and Biological Engineering",
                "College of Engineering",
                "Environmental and Safety",
                "Engineering Civil System Engineering",
                "Transportation System Engineering",
                "Architecture Engineering Major(4-years) Architecture(5 year)"
            ],
            "College of Information Technology": [
                "Electrical and Computer Engineering"
            ],
            "College of Computing and Informatics": [
                "Software and Computer Engineering",
                "Cyber Security",
                "Digital Media"
            ],
            "College of Natural Sciences": [
                "Mathematics",
                "Physics",
                "Chemistry",
                "Biological Science"
            ],
            "College of Humanities": [
                "Korean Language and Literature",
                "English Language and Literature",
                "French Language Literature",
                "History",
                "Culture and Contents"
            ],
            "College of Social Sciences": [
                "Economics",
                "Public Administration",
                "College of Social Sciences",
                "Psychology",
                "Sociology",
                "Political Science and Diplomacy"
            ]
        }
    },
    "Chonnam National University": {
        "english_track": {
            "Departments": ["Not available"]
        },
        "korean_track": {
            "AI Convergence": [
                "Artificial Intelligence",
                "Intelligent Mobility Nursing: Nursing"
            ],
            "Business Administration:": [
                "Business Administration",
                "Economics"
            ],
            "Engineering": [
                "School of Architecture",
                "School of Architecture (Major of Architectural Engineering)",
                "School of Architecture",
                "Major of Architecture & Urban Design",
                "School of Polymer Science Engineering",
                "School of Mechanical Engineering",
                "Department of Industrial Engineering",
                "Department of Biotechnology & Bioengineering",
                "School of Materials Science and Engineering",
                "Department of Energy and Resources Engineering",
                "Department of Electrical Engineering",
                "School of Electronic and Computer Engineering",
                "Department of Civil Engineering",
                "School of Chemical Engineering"
            ],
            "Agriculture and Life Sciences": [
                "Department of Agricultural Economics",
                "Department of Agricultural & Biological Chemistry",
                "Division of Animal Science",
                "Department of Bioenergy Science and Technology",
                "Department of Molecular Biotechnology",
                "Department of Forest Resources",
                "Department of Food Science & Technology",
                "Department of Horticulture",
                "Department of Convergence Biosystems Engineering",
                "Department of Applied Biology",
                "Department of Applied Plant Science",
                "Department of Wood Science & Engineering",
                "Department of Landscape Architecture",
                "Department of Rural and Biosystems Engineering"
            ],
            "Social Sciences": [
                "Department of Library and Information Science",
                "Department of Cultural Anthropology and Archaeology",
                "Media and Communication",
                "Communication",
                "Department of Sociology",
                "Department of Psychology",
                "Department of Political Science and Intemational Relations",
                "Department of Geography",
                "Department of Public Administration"
            ],
            "Human Ecology": [
                "Department of Family Environment and Welfare",
                "Division of Food and Nutrition",
                "Department of Clothing and Textiles"
            ],
            "Arts": [
                "Korean Traditional Music",
                "Design",
                "Fine Arts",
                "Major of Korean Painting",
                "Western Painting",
                "Sculpture",
                "Crafts Fine Arts",
                "Theory of Arts",
                "Music"
            ],
            "Humanities": [
                "Korean Language & Literature",
                "German Language & Literature",
                "French Language & Literature",
                "History",
                "English Language & Literature",
                "Japanese Language & Literature",
                "Chinese Language & Literature",
                "Philosophy"
            ],
            "Natural Sciences": [
                "Physics",
                "Biological Sciences and Technology",
                "Biological Science & Technology - Major of Biological Science / Major of Systems Biology",
                "Biology",
                "Mathematics",
                "Earth Systems & Environmental Science",
                "Statistics",
                "Chemistry"
            ],
            "Engineering (Yeo-su Campus)": [
                "Department of Architecture Design",
                "Department of Mechanical Design Engineering",
                "Department of Mechanical System Engineering",
                "Department of Refrigeration & Air-conditioning Engineering",
                "Department of Mechatronics Engineering",
                "Department of Petrochemical Materials Engineering",
                "Department of Integrative Biotechnology",
                "Department of Biomedical Engineering",
                "School of Electrical and Computer Engineering",
                "School of Electrical and Computer Engineering- Major Electrical and Semiconductor Engineering",
                "School of Electrical and Computer Engineering",
                "Major in Computer Engineering",
                "Department of Electronic Communication Engineering",
                "School of Healthcare and Biomedical Engineering",
                "Department of Chemical and Biomolecular Engineering",
                "Culture & Social Sciences: Department of English Studies",
                "Department of Japanese Studies",
                "Department of Chinese Studies",
                "Division of Global Business",
                "Department of Cultural Tourism Management",
                "Department of Logistics and Transportation",
                "Division of Culture Contents",
                "Division of Culture Contents - Department of Multimedia / Electronic Commerce"
            ],
            "Fisheries & Ocean Sciences": [
                "Department of Power System Engineering",
                "Department of Aqualife Medicine",
                "Department Smart Fisheries Resources Management",
                "Department of Aquaculture",
                "Department of Naval Architecture and Ocean Engineering",
                "Department of Maritime Police Science",
                "Department of Marine Bio food Science",
                "Department of Marine Production Management",
                "Department of Ocean Integrated Science"
            ]
        }
    },
    "Chung Ang University": {
        "english_track": {
            "Departments": ["Chung Ang University does not offer courses in English, but you can apply with your English language test score and once you get accepted, you will required to study Korean language program first."]
        },
        "korean_track": {
            "Humanities": [
                "Korean Language & Literature",
                "English Language & Literature",
                "European Languages & Cultures",
                "Asian Languages & Cultures",
                "Philosophy",
                "History"
            ],
            "Social Sciences": [
                "Political Science",
                "Public Administration",
                "Psychology",
                "Library & Information Science",
                "Social Welfare",
                "Media Communication",
                "Sociology",
                "Urban Planning and Real Estate"
            ],
            "Business & Economics": [
                "Business Administration",
                "Economics",
                "Applied Statistics",
                "Advertising & Public Relations",
                "International Logistics"
            ],
            "Natural Sciences": [
                "Physics",
                "Chemistry",
                "Biological Sciences",
                "Mathematics"
            ],
            "Biotechnology and Natural Resources": [
                "Bioresource & Bioscience",
                "Food Science & Technology"
            ],
            "Engineering": [
                "Civil & Environmental Engineering",
                "Urban Design & Studies",
                "Architecture & Building Science",
                "Chemical Engineering & New Material Science",
                "Mechanical Engineering"
            ],
            "ICT Engineering": [
                "Electrical and Electronics Engineering",
                "Software"
            ],
            "Arts": [
                "Performing Arts and Media",
                "Design",
                "Korean music",
                "Global School of Arts"
            ],
            "Sport": [
                "Sports Science"
            ]
        }
    },
    "Chungnam National University": {
        "english_track": {
            "International Studies": [
                "International Studies"
            ]
        },
        "korean_track": {
            "Humanities": [
                "Korean Language and Literature",
                "English Language and Literature",
                "German Language and Literature",
                "French Language and Literature",
                "Chinese Language and Literature",
                "Japanese Language and Literature",
                "Sino-Korean Literature",
                "Linguistics",
                "History",
                "Korean History",
                "Archaeology",
                "Philosophy"
            ],
            "Social Sciences": [
                "Sociology",
                "Library and Information Science",
                "Psychology",
                "Communication",
                "Social Welfare",
                "Political Science and Diplomacy",
                "Public Administration",
                "Autonomy and Urban Administration"
            ],
            "Economics and Management": [
                "Business Administration",
                "International Trade"
            ],
            "Natural Sciences": [
                "Mathematics",
                "Information and Statistics",
                "Physics",
                "Astronomy and Space Science",
                "Chemistry",
                "Biochemistry",
                "Marine Environmental Sciences",
                "Geological Sciences"
            ],
            "Engineering": [
                "Architecture(5-year program)",
                "Civil Engineering",
                "Mechanical Engineering",
                "Aerospace Engineering",
                "Materials Science and Engineering",
                "Organic Materials Engineering",
                "Chemical Engineering and Applied Chemistry",
                "Electrical Engineering"
            ],
            "Agriculture and Life Sciences": [
                "Agricultural Economics",
                "Crop Science",
                "Horticultural Science",
                "Environmental and Forest Resources",
                "Biobased Materials",
                "Applied Biology",
                "Animal and Dairy Science",
                "Agricultural and Rural Engineering",
                "Biosystems Machinery Engineering",
                "Food Science and Technology",
                "Bio-Environmental Chemistry"
            ],
            "Human Ecology": [
                "Clothing and Textiles",
                "Consumer Science"
            ],
            "Bioscience and Biotechnology": [
                "Biological Sciences",
                "Microbiology and Molecular Biology"
            ],
            "Art, Music and Physical Education": [
                "Dance(Korean dance)",
                "Dance(modern dance)",
                "Dance(ballet)",
                "Sport Science",
                "Fine Art"
            ]
        }
    },
    "DGIST": {
        "english_track": {
            "Engineering": [
                "Physics",
                "Chemistry",
                "Life Sciences",
                "Mechanical Engineering",
                "Material Science and Engineering",
                "Electronic Engineering",
                "Computer Science and Engineering",
                "Chemical Engineering"
            ]
        },
        "korean_track": {
            "Departments": ["Please refer to DGIST website in Korean"]
        }
    },
    "Ewha Womans University": {
        "english_track": {
            "Scranton College": [
                "Division of International Studies",
                "Global Korean Studies"
            ]
        },
        "korean_track": {
            "College of Liberal Arts": [
                "Korean Language & Literature",
                "Chinese Language & Literature",
                "French Language & Literature",
                "German Language & Literature History",
                "Philosophy Christian Studies",
                "Division of English Language & Literature",
                "Public Administration",
                "Economics",
                "Library & Information Science",
                "Sociology",
                "Social Welfare",
                "Psychology",
                "Consumer Studies",
                "Division of Communication & Media"
            ],
            "College of Social Sciences": [
                "Political Science & International Relations"
            ],
            "College of Natural Sciences": [
                "Mathematics",
                "Statistics",
                "Physics",
                "Division of Molecular Life and Chemical Science"
            ],
            "College of Engineering": [
                "Division of Electronic and Semiconductor Engineering",
                "Food Science and Biotechnology",
                "Chemical Engineering and Materials Science",
                "Architecture (5-year program)",
                "Architectural and Urban Systems Engineering",
                "Environmental Science and Engineering",
                "Climate and Energy Systems Engineering",
                "Mechanical and Biomedical Engineering"
            ],
            "College of Music": [
                "Keyboard Instruments",
                "Orchestral Instruments",
                "Voice Composition",
                "Korean Music",
                "Dance"
            ],
            "College of Art & Design": [
                "Division of Fine Arts",
                "Division of Design",
                "Division of Fiber & Fashion"
            ],
            "College of Business Administration": [
                "Division of Business Administration"
            ],
            "College of Science & Industry Convergence": [
                "Content Convergence",
                "Fashion Industry",
                "International Office Administration",
                "Nutritional Science & Food Management",
                "Health Convergence",
                "Division of Kinesiology & Sports Studies"
            ],
            "College of Artificial Intelligence": [
                "Computer Science and Engineering",
                "Cyber Security"
            ]
        }
    },
    "GIST": {
        "english_track": {
            "College of Engineering": [
                "Electrical Engineering and Computer Science",
                "Materials Science and Engineering",
                "Mechanical Engineering",
                "Earth Sciences and Environmental Engineering",
                "Life Sciences",
                "Physics",
                "Chemistry"
            ]
        },
        "korean_track": {
            "Departments": ["Please refer to GIST website in Korean."]
        }
    },
    "Hanyang University": {
        "english_track": {
            "Engineering": [
                "Data Science"
            ],
            "Business": [
                "Business Administration"
            ],
            "International Studies": [
                "Global Korean Studies",
                "International Studies"
            ]
        },
        "korean_track": {
            "Engineering": [
                "Architecture (5-year program)",
                "Architectural Engineering (4-year program)",
                "Civil and Environmental Engineering",
                "Urban Planning and Engineering",
                "Earth Resources and Environmental Engineering",
                "Electronic Engineering",
                "Computer Science",
                "Information Systems",
                "Electrical and Biomedical Engineering",
                "Materials Science and Engineering",
                "Chemical Engineering",
                "Bioengineering",
                "Organic and Nano Engineering",
                "Energy Engineering",
                "Mechanical Engineering",
                "Nuclear Engineering",
                "Industrial Engineering",
                "Automotive Engineering"
            ],
            "Humanities": [
                "Korean Language & Literature",
                "Chinese Language & Literature",
                "English Language & Literature",
                "German Language & Literature",
                "History",
                "Philosophy",
                "Korean Language & Literature",
                "English Language & Literature"
            ],
            "Social Sciences": [
                "Political Science & International Studies",
                "Sociology",
                "Media Communication",
                "Tourism"
            ],
            "Natural Sciences": [
                "Mathematics",
                "Physics",
                "Chemistry",
                "Life Science"
            ],
            "Policy Science": [
                "Policy Studies",
                "Public Administration"
            ],
            "Economics&Finance": [
                "Economics & Finance"
            ],
            "Business": [
                "Business Administration",
                "Finance"
            ],
            "Human Ecology": [
                "Clothing & Textiles",
                "Food & Nutrition",
                "Interior Architecture Design"
            ],
            "Music": [
                "Voice",
                "Composition",
                "Piano",
                "Orchestral Music",
                "Korean Traditional Music"
            ],
            "Performing Arts and Sports": [
                "Sport Industry and Science",
                "Theater and Film",
                "Dance"
            ]
        }
    },
    "Hankuk University of Foreign Studies": {
        "english_track": {
            "College of English": [
                "English Linguistics and Language Technology (ELLT)"
            ],
            "Division of International Studies": [
                "International Studies"
            ]
        },
        "korean_track": {
            "College of Occidental Languages": [
                "English Literature and Culture English for International Conferences and Communication (EICC)"
            ],
            "College of Asian Languages & Culture": [
                "Division of French Language",
                "German",
                "Russian",
                "Spanish",
                "Italian",
                "Portuguese",
                "Dutch",
                "Scandinavian Languages"
            ],
            "College of Chinese": [
                "Malay-Indonesian",
                "Arabic",
                "Thai",
                "Vietnamese",
                "Hindi",
                "Turkish and Azerbaijani",
                "Persian and Iranian Studies",
                "Mongolian"
            ],
            "College of Japanese": [
                "Chinese Language",
                "Literature and Culture China Data Curation",
                "Chinese Foreign Affairs and Commerce"
            ],
            "College of Business and Economics": [
                "Japanese Language",
                "Literature and Culture",
                "Integrated Japanese Studies",
                "Public Administration",
                "Media Communication Division"
            ],
            "College of Social Science": [
                "Political Science and Diplomacy"
            ],
            "College of Business": [
                "Economics"
            ],
            "College of Education": [
                "Business Administration"
            ],
            "College of AI Convergence:": [
                "English Education",
                "Korean Education French Education",
                "German Education",
                "Chinese Education"
            ],
            "Division of KFL": [
                "Social Science & AI",
                "Language & AI"
            ],
            "College of Humanities": [
                "Korean Education as a Foreign Language",
                "Korean Interpretation and Translation as a Foreign Language"
            ],
            "College of Central and East European Studies": [
                "Department of Philosophy",
                "Department of History",
                "Department of Linguistics and Cognitive Science"
            ],
            "College of International and Area Studies": [
                "Greek and Bulgarian Studies",
                "Central Asian Studies",
                "African Studies",
                "Korean Studies",
                "Polish",
                "Romanian",
                "Czech and Slovak Studies",
                "Hungarian",
                "South Slavic Studies Ukrainian Studies"
            ],
            "College of Business and Economics:.1": [
                "Global Business & Technology International Finance"
            ],
            "College of Natural Science": [
                "Mathematics",
                "Statistics",
                "Electronic Physics",
                "Environmental Science",
                "Bioscience and Biotechnology",
                "Chemistry"
            ],
            "College of Engineering:": [
                "Computer Engineering",
                "Information Communications Engineering",
                "Division of Semiconductor & Electronics Engineering",
                "Industrial and Management Engineering"
            ],
            "Ingenium College of Convergence Studies": [
                "Computer Engineering",
                "Information Communications Engineering",
                "Division of Semiconductor & Electronics Engineering",
                "Industrial and Management Engineering",
                "Faculty of Convergence Studies"
            ],
            "College of Culture & Technology": [
                "Division of Digital Contents",
                "Division of Tourism & Wellness",
                "Division of Global Sport Industry"
            ],
            "College of AI Convergence": [
                "AI Data Convergence",
                "Finance & AI Convergence"
            ],
            "Division of Biomedical Engineering": [
                "Biomedical Engineering Studies"
            ],
            "Global Open Major Division:": [
                "Global Open Major Division:"
            ],
            "Division of Climate Changes": [
                "Climate Changes"
            ]
        }
    },
    "Inha University": {
        "english_track": {
            "School of Global Convergence Studies": [
                "International Business & Trade",
                "Integrated System Engineering",
                "Korean Language & Culture"
            ]
        },
        "korean_track": {
            "College of Engineering": [
                "Mechanical Engineering",
                "Aerospace Engineering",
                "Naval Architecture & Ocean Engineering",
                "Industrial Engineering",
                "Chemical Engineering",
                "Polymer Science and Engineering",
                "Materials Science Engineering",
                "Civil Engineering",
                "Environmental Engineering",
                "Geo-informational Engineering",
                "Faculty of Architecture",
                "Energy Resources Engineering",
                "Electrical Engineering",
                "Electronic Engineering",
                "Information and Communication Engineering"
            ],
            "Department of Biological science:": [
                "Biological Engineering",
                "Biological Sciences"
            ],
            "College of Software and Convergence": [
                "Computer Engineering"
            ],
            "College of Natural Science": [
                "Mathematics",
                "Statistics",
                "Physics",
                "Chemistry",
                "Ocean Sciences",
                "Food and Nutrition"
            ],
            "College of Business Administration:": [
                "Business Administration",
                "Global Finance and Banking",
                "Asia Pacific School of Logistics",
                "International Trade"
            ],
            "College of Social Science": [
                "Public Administration",
                "Political Science and International Relations",
                "Media Communication",
                "Economics",
                "Consumer Science",
                "Child Studies",
                "Social Welfare Studies"
            ],
            "College of Humanities:": [
                "Korean Language and Literature",
                "History",
                "Philosophy",
                "China Studies",
                "Japanese Language and Culture",
                "English Language and Literature",
                "French Language and Culture",
                "Cultural Contents and Management"
            ],
            "College of Medicine": [
                "Nursing"
            ],
            "College of Education:": [
                "Physical Education"
            ],
            "College of Arts and Sports": [
                "Fine Arts",
                "Design Convergence",
                "Kinesiology",
                "Theater and Film Studies",
                "Fashion Design and Textiles"
            ]
        }
    },
    "Jeonbuk National University": {
        "english_track": {
            "Global Convergence College": [
                "School of International Engineering and Science",
                "The School of International Studies"
            ]
        },
        "korean_track": {
            "University Headquarter": [
                "Smart Farm"
            ],
            "Global Convergence College": [
                "Public Policy"
            ],
            "Engineering": [
                "Architectural Engineering",
                "Mechanical Engineering",
                "Mechanical Design Engineering (Mechanical Design Engineering)",
                "Mechanical Design Engineering (Nano-Bio Mechanical System Engineering)",
                "Mechanical System Engineering",
                "Urban Engineering",
                "Biomedical Engineering",
                "Industrial and Information Systems Engineering",
                "Software Engineering",
                "New Materials Engineering (Electronic materials Engineering)",
                "Quantum System Engineering",
                "Division of Convergence Technology Engineering (Major of IT Convergence Mechatronics Engineering)",
                "Division of Convergence Technology",
                "Engineering (Major of IT Applied System Engineering)",
                "Computer Science",
                "Engineering and Artificial Intelligence",
                "Division of Civil/Environmental/Mineral Resources and Energy Engineering (Mineral Resources&Energy Engineering)",
                "Division of Civil/Environmental/Mineral Resources and Energy Engineering (Civil Engineering)",
                "Division of Civil/Environmental/Mineral Resources and Energy Engineering (Environmental Engineering)"
            ],
            "Agriculture and Life Sciences:": [
                "Division of Agricultural",
                "Economics and Food Marketing (Food Marketing)",
                "Division of Agricultural Economics and Food Marketing (Agricultural Economics)",
                "Agricultural Biology",
                "Animal Biotechnology",
                "Wood Science and Technology",
                "Forest Environment Science",
                "Food Science and Technology",
                "Horticulture",
                "Crop Agriculture and Life Science",
                "Landscape Architecture",
                "Rural Construction Engineering"
            ],
            "Education": [
                "English Education"
            ],
            "Social Science:": [
                "Social Welfare",
                "Sociology",
                "Media and Communication Studies",
                "Psychology",
                "Political Science & Diplomacy",
                "Public Administration"
            ],
            "Commerce": [
                "Business Administration",
                "Economics",
                "International Trade",
                "Accounting"
            ],
            "Human Ecology": [
                "Child Studies",
                "Fashion Design",
                "Housing Environmental Design"
            ],
            "Arts": [
                "Dance (Ballet/Dance Education Creator)",
                "Dance (Korea Folk Dance)",
                "Dance (Contemporary Dance/Choreography)",
                "Industrial Design (Product Design)",
                "Industrial Design (Visual-Media Design)",
                "Music(Composition)",
                "Music(Voice)",
                "Music(Piano)",
                "Music(Wind Music)",
                "Music(String)",
                "Korean Music (Korean Traditional Theory/ Composition)",
                "Korean Music (Vocal/Percussion Music)",
                "Korean Music (Wind Music)",
                "Korean Music (String Music)"
            ],
            "Humanities": [
                "Archaeology and Cultural Anthropology",
                "Korean Language & Literature",
                "German Studies",
                "Library and Information Science",
                "Spanish & Latin american studies",
                "English Language and Literature",
                "Japanese Studies",
                "Chinese Language & Literature",
                "Philosophy",
                "French African Studies"
            ],
            "Natural Sciences:": [
                "Science studies",
                "Physics",
                "Division of Life Sciences (Molecular Biology Major)",
                "Division of Life Sciences (Life Sciences Major)",
                "Sport Science",
                "Earth & Environmental Sciences"
            ]
        }
    },
    "KAIST": {
        "english_track": {
            "College of Natural Sciences": [
                "Physics",
                "Mathematical Sciences",
                "Chemistry",
                "Brain and Cognitive Sciences"
            ],
            "College of Life Science & Bioengineering": [
                "Biological Sciences"
            ],
            "College of Engineering": [
                "Mechanical Engineering",
                "Aerospace Engineering",
                "Electrical Engineering",
                "Computer Science",
                "Civil & Environmental Engineering",
                "Bio & Brain Engineering",
                "Industrial Design",
                "Industrial & Systems Engineering",
                "Chemical & Biomolecular Engineering",
                "Materials Science & Engineering",
                "Nuclear & Quantum Engineering"
            ],
            "College of Business": [
                "Business and Technology Management"
            ]
        },
        "korean_track": {
            "Departments": [
                "Please refer to KAIST website"
            ]
        }
    },
    "Konkuk University": {
        "english_track": {
            "Departments": ["Not available"]
        },
        "korean_track": {
            "College of Art and Design": [
                "Department of Industrial Design",
                "Department of Interior Design",
                "Department of Fashion Design",
                "Department of Visual Communication & Media Design",
                "Department of Media Contents",
                "Department of Formative Arts"
            ],
            "College of Humanities and Social Sciences": [
                "Department of Business Administration",
                "Department of Economics and Trade",
                "Department of Police Science",
                "Department of Fire and Disaster Prevention",
                "Department of Library and Information Science",
                "Department of Social Welfare",
                "Department of Mass Communication",
                "Department of Children's Literature and Korean Lang. & Lit.",
                "Department of English Language and Culture"
            ],
            "College of Science and Technology": [
                "Department of Mechatronics Engineering",
                "Department of Computer Engineering",
                "Department of Biomedical Engineering",
                "Department of Green Technology Convergence",
                "Department of Energy Materials Science & Engineering"
            ],
            "College of Biomedical and Health Science:": [
                "Department of Medicinal Biosciences",
                "Department of Biotechnology",
                "Department of Food and Nutrition Science",
                "Department of Beauty Cosmetics",
                "Department of Sport and Health Studies",
                "Department of Golf Industry"
            ]
        }
    },
    "Korea University": {
        "english_track": {
            "College of International Studies": [
                "International Studies",
                "Global Korean Studies"
            ]
        },
        "korean_track": {
            "Korea University Business School": [
                "Business Administration"
            ],
            "College of Liberal Arts": [
                "Korean Language and Literature",
                "Philosophy",
                "Korean History",
                "History",
                "Sociology",
                "Sinographic Literatures",
                "English Language and Literature",
                "German Language and Literature",
                "French Language and Literature",
                "Chinese Language and Literature",
                "Russian Language and Literature",
                "Japanese Language and Literature",
                "Spanish Language and Literature",
                "Linguistics"
            ],
            "College of Life Sciences & Biotechnology": [
                "Life Sciences",
                "Biotechnology",
                "Food Bioscience and Technology",
                "Environmental Science and Ecological Engineering",
                "Food and Resource Economics"
            ],
            "College of Political Science and Economics": [
                "Political Science and International Relations",
                "Economics",
                "Statistics",
                "Public Administration"
            ],
            "College of Science": [
                "Mathematics",
                "Physics",
                "Chemistry",
                "Earth and Environmental Science"
            ],
            "College of Engineering": [
                "Chemical & Biological Engineering",
                "Materials Science & Engineering",
                "Civil",
                "Environmental",
                "& Architectural Engineering",
                "Architecture (5 years)",
                "Mechanical Engineering",
                "Industrial Management Engineering",
                "Electrical Engineering",
                "Integrative Energy Engineering"
            ],
            "College of Education": [
                "Education",
                "Korean Language Education",
                "English Education",
                "Geography Education",
                "History Education",
                "Home Economics Education",
                "Mathematics Education",
                "Physical Education"
            ],
            "College of Informatics": [
                "Computer Science and Engineering",
                "Data Science"
            ],
            "College of Art & Design": [
                "Art & Design"
            ],
            "College of Media & Communication": [
                "Media & Communication"
            ],
            "College of Health Science": [
                "Biomedical Engineering",
                "Biosystems & Biomedical Science",
                "Health Environmental Science",
                "Health Policy & Management"
            ],
            "College of Interdisciplinary Studies": [
                "Interdisciplinary Studies"
            ],
            "College of Smart Security": [
                "Smart Security"
            ],
            "College of Psychology": [
                "Psychology"
            ]
        }
    },
    "Kyung Hee University": {
        "english_track": {
            "College of Management": [
                "Department of Management"
            ],
            "College of Hotel and Tourism Management": [
                "Department of Global Hospitality & Tourism Management"
            ],
            "College of International Studies": [
                "Department of International Studies",
                "Department of Global Korean Studies"
            ]
        },
        "korean_track": {
            "College of Humanities": [
                "Department of Korean Language and Literature",
                "Department of History",
                "Department of Philosophy",
                "Department of English Language and Linguistics",
                "Department of Applied English Interpretation and Translation"
            ],
            "College of Global Eminence": [
                "Department of Global Eminence"
            ],
            "College of Politics and Economics": [
                "Department of Political Science",
                "Department of Public Administration",
                "Department of Sociology",
                "Department of Economics",
                "Department of International Business and Trade",
                "Department of Media"
            ],
            "College of Management": [
                "Department of Management",
                "Department of Accounting and Taxation"
            ],
            "College of Hotel and Tourism Management": [
                "Department of Hospitality Management",
                "Department of Culinary Arts & Food Design Management",
                "School of Tourism and Entertainment",
                "Department of Hospitality Management",
                "Department of Tourism"
            ],
            "College of Human Ecology": [
                "Department of Child and Family Studies",
                "Department of Housing and Interior Design",
                "Department of Clothing and Textiles",
                "Department of Food and Nutrition"
            ],
            "College of Science": [
                "Department of Mathematics",
                "Department of Physics",
                "Department of Chemistry",
                "Department of Biology",
                "Department of Geography",
                "Department of Information Display"
            ],
            "College of Engineering": [
                "Department of Mechanical Engineering",
                "Department of Industrial & Management Engineering",
                "Department of Nuclear Engineering",
                "Department of Chemical Engineering",
                "Department of Advanced Materials Engineering for Information & Electronics",
                "Department of Civil Engineering",
                "Department of Architectural Engineering",
                "Department of Environmental Science and Engineering"
            ],
            "College of Electronics and Information": [
                "Department of Electronic Engineering",
                "Department of Biomedical Engineering"
            ],
            "College of Software Convergence": [
                "Department of Computer Engineering",
                "Department of Software Convergence",
                "Department of Artificial Intelligence"
            ],
            "College of Applied Science": [
                "Department of Applied Mathematics",
                "Department of Applied Physics",
                "Department of Applied Chemistry",
                "Department of Astronomy and Space Science"
            ],
            "College of Life Sciences": [
                "Department of Genetics and Biotechnology",
                "Department of Food Science & BIO Technology",
                "Department of Oriental Medicine Biotechnology",
                "Department of Plant & Environmental New Resources",
                "Department of Smart-Farm Science"
            ],
            "College of Foreign Language": [
                "Department of French",
                "Department of Spanish",
                "Department of Russian",
                "Department of Chinese",
                "Department of Japanese",
                "Department of Korean",
                "Department of Global Communication"
            ],
            "College of Art and Design": [
                "Department of Industrial Design",
                "Department of Visual Design",
                "Department of Landscape Architecture",
                "Department of Textile and Clothing Design",
                "Department of Digital Contents",
                "Department of Ceramics",
                "Department of Postmodern Music",
                "Department of Theater & Film"
            ],
            "College of Physical Education:": [
                "Department of Physical Education",
                "Department of Sports Medicine",
                "Department of Golf Industry",
                "Department of Taekwondo",
                "Department of Coaching"
            ]
        }
    },
    "Kyungpook National University": {
        "english_track": {
            "Departments": [
                "International Studies Department"
            ]
        },
        "korean_track": {
            "Humanities": [
                "Korean Language & Literature",
                "English Language & Literature",
                "History",
                "Philosophy",
                "French Language & Literature",
                "German Language Literature",
                "Chinese Language & Literature",
                "Archaeology & Anthropology",
                "Japanese Language & Literature",
                "Korean Literature in Classical Literature Chinese",
                "Russian Language & Literature"
            ],
            "Social Sciences": [
                "Political Science & Diplomacy",
                "Sociology",
                "Library & Information Science",
                "Geography",
                "Psychology",
                "Social Welfare",
                "Media and Communication"
            ],
            "Natural Sciences:": [
                "Mathematics",
                "Physics",
                "Chemistry",
                "Biotechnology",
                "Earth System Science",
                "Biology",
                "Natural Sciences",
                "Statistics"
            ],
            "Economic & Business Administration": [
                "Business Administration",
                "Economics & Trade"
            ],
            "Engineering": [
                "Materials Science and Metallurgical Engineering",
                "Advanced Materials",
                "Science and Engineering",
                "Mechanical Engineering",
                "Architecture(Architecture)",
                "Architecture",
                "Engineering",
                "Civil Engineering",
                "Architecture (Architectural Engineering)",
                "Applied Chemistry",
                "Chemical Engineering",
                "Polymer Science and Engineering",
                "Textile System Engineering",
                "Environmental Energy Engineering"
            ],
            "IT Engineering": [
                "Electronics Engineering",
                "Electronics Engineering(Artificial Intelligence)",
                "Computer Science and Engineering (Platform Engineering Software & Data Science)",
                "Computer Science and Engineering (Artificial Intelligence Computing)",
                "Computer Science and Engineering (Global software convergence)",
                "Computer Science and Engineering (Global Software Convergence)",
                "Electrical Engineering"
            ],
            "Agriculture and Life Sciences": [
                "Applied Bioscience",
                "Plant Medicine",
                "Food Science & Horticultural Sciences",
                "Biotechnology",
                "Agriculture &Life Sciences",
                "Forest Sciences and Bio-fibers and Materials Science",
                "Landscaper",
                "Agricultural Civil Engineering",
                "Smart Bio-Industrial Mechanical Engineering",
                "Food and Resource Economics"
            ],
            "Music and Arts": [
                "Korean Traditional Music"
            ],
            "Teachers College": [
                "History Education"
            ],
            "Human Ecology": [
                "Child Studies",
                "Clothing and Textiles",
                "Human Ecology",
                "Food Science and Nutrition"
            ],
            "Public Administration": [
                "Public Administration:"
            ],
            "Ecology &Environmental Science": [
                "Plant Resources",
                "Entomology",
                "Animal Science",
                "Forest Ecology and Protection",
                "Horse/Companion and wild Animal Science",
                "Animal Biotechnology",
                "Tourism",
                "Kinesiology (Sport Studies)"
            ],
            "Science &Technology": [
                "Construction and Disaster Prevention Engineering",
                "Environmental and Safety Engineering",
                "Precision Mechanical Engineering",
                "Automotive Engineering",
                "Nano & Advanced Materials Science and Engineering",
                "Software",
                "Energy Chemical Engineering",
                "Food and Food Service Industry",
                "Textile Fashion",
                "Textile Fashion Design(Fashion Design)",
                "Design (Textile Engineering)",
                "Location-Based Information System",
                "Smart Plant Engineering"
            ]
        }
    },
    "Pusan National University": {
        "english_track": {
            "College of Economics & International Trade": [
                "Department of Global Studies"
            ]
        },
        "korean_track": {
            "College of Humanities": [
                "Department of Korean Language and Literature",
                "Department of Chinese Language and Literature",
                "Department of Japanese Language and Literature",
                "Department of English Language and Literature",
                "Department of French Language and Literature",
                "Department of German Language and Literature",
                "Department of Russian Language and Literature",
                "Department of Korean Literature in Chinese Characters",
                "Department of Language and Information Department of History",
                "Department of Philosophy",
                "Department of Archaeology"
            ],
            "College of Social Sciences:": [
                "Department of Public Administration",
                "Department of Political Science and Diplomacy",
                "Department of Social Welfare",
                "Department of Sociology",
                "Department of Psychology",
                "Department of Library",
                "Archive and Information Studies",
                "Department of Media & Communication"
            ],
            "College of Economics & International Trade": [
                "Department of Public Administration",
                "Department of Political Science and Diplomacy",
                "Department of Social Welfare",
                "Department of Sociology",
                "Department of Psychology",
                "Department of Library",
                "Archive and Information Studies",
                "Department of Media & Communication"
            ],
            "School of Business": [
                "Department of International Trade",
                "Department of Economics",
                "Department of Tourism and Convention",
                "Department of Public Policy & Management"
            ],
            "College of Human Ecology:": [
                "Department of Child Development and Family Studies"
            ],
            "College of Natural Resources & Life Sciences": [
                "Department of Food and Resource Economics"
            ],
            "College of Natural Sciences": [
                "Department of Mathematics",
                "Department of Statistics",
                "Department of Physics",
                "Department of Chemistry",
                "Department of Biological Sciences",
                "Department of Microbiology",
                "Department of Molecular Biology",
                "Department of Geological Sciences",
                "Department of Atmospheric Environmental Sciences",
                "Department of Oceanography"
            ],
            "College of Engineering": [
                "School of Mechanical Engineering",
                "Department of Polymer Science and Engineering",
                "Department of Organic Material Science and Engineering",
                "School of Chemical Biomolecular and Environmental Engineering (Environmental Engineering Major",
                "Chemical and Biomolecular Engineering Major)",
                "School of Materials Science and Engineering",
                "School of Electrical and Electronics Engineering(Electrical Engineering Major)",
                "School of Electrical and Electronics Engineering(Electronics Engineering Major)",
                "School of Electrical and Electronics Engineering(Semiconductor Engineering Major)",
                "Department of Architecture(5-year program)",
                "Department of Architectural Engineering",
                "Department of Urban Planning & Engineering",
                "Department of Civil Engineering",
                "Department of Aerospace Engineering",
                "Department of Industrial Engineering",
                "Department of Naval Architecture and Ocean Engineering"
            ],
            "College of Nursing": [
                "Department of Nursing"
            ],
            "College of Human Ecology": [
                "Department of Clothing and Textiles",
                "Department of Food Science and Nutrition",
                "Department of Interior & Environmental Design"
            ],
            "College of Natural Resources & Life Sciences:.1": [
                "Department of Plant Bioscience",
                "Department of Horticultural Bioscience",
                "Department of Animal Science",
                "Department of Food Science & Technology",
                "Department of Life Science & Environmental Biochemistry",
                "Department of Biomaterial Science",
                "Department of Bio-Industrial Machinery Engineering",
                "Department of Applied Information Technology and Engineering",
                "Department of Bioenvironmental Energy",
                "Department of Landscape Architecture"
            ],
            "College of Information and BioMedical Engineering": [
                "School of BioMedical Convergence Engineering",
                "School of Computer Science and Engineering (Computer Engineering Major",
                "Artificial Intelligence Major)"
            ],
            "College of Arts": [
                "Department of Music (Vocal Music",
                "Composition)",
                "Department of Fine Arts (Carving & Modeling",
                "Korean Painting",
                "Western Painting)",
                "Department of Plastic Arts (Wooden Furniture Painting",
                "Ceramics",
                "Textiles & Metal)",
                "Department of Korean Music (String Vocal Wind Percussion Theory Composition)",
                "Department of Dance (Korean Dance Ballet Modern Dance)",
                "Department of Design (Visual Design, Animation Design & Technology )",
                "Department of Art Culture and Image"
            ]
        }
    },
    "Sejong University": {
        "english_track": {
            "Liberal Arts": [
                "Division of Global Leadership"
            ],
            "Social Sciences": [
                "Public Administration",
                "Media and Communication"
            ],
            "Business and Economics": [
                "Faculty of Business Administration",
                "Economics"
            ],
            "Hospitality and Tourism Management": [
                "Faculty of Hospitality, Tourism and Food Service Management"
            ],
            "College of Convergence": [
                "Computer Science and Engineering"
            ],
            "Education": [
                "Fashion Design",
                "Music"
            ]
        },
        "korean_track": {
            "Liberal Arts": [
                "Korean Language and Literature",
                "International Studies",
                "History",
                "Education"
            ],
            "Social Sciences": [
                "Law"
            ],
            "Business and Economics": [
                "Faculty of Business Administration"
            ],
            "Hospitality and Tourism Management": [
                "Faculty of Hospitality,Tourism and Food Service Management"
            ],
            "Natural Sciences": [
                "Mathematics and Statistics",
                "Faculty of Mathematics",
                "Physics and Astronomy",
                "Chemistry"
            ],
            "Life Sciences": [
                "Faculty of Biological Systems",
                "Integrative Biological Sciences and Industry"
            ],
            "College of Convergence": [
                "Electrical Engineering",
                "Semiconductor Systems Engineering",
                "Computer and Information Security",
                "Software",
                "Artificial Intelligence and Robotics",
                "Artificial Intelligence and Data Science",
                "School of Intelligent Mechatronics Engineering",
                "Creative Studies",
                "Data Science",
                "Artificial Intelligence"
            ],
            "Engineering": [
                "Architectural Engineering",
                "Architecture",
                "Civil and Environmental Engineering",
                "Environment",
                "Energy & Geoinformatics",
                "Energy Resources and Geosystems Engineering",
                "School of Aerospace and Drone Engineering",
                "Faculty of Mechanical and Aerospace Engineering",
                "Nano Technology and Advanced Materials Engineering",
                "Quantum and Nuclear Engineering"
            ],
            "Education": [
                "Painting",
                "Physical Education",
                "Dance",
                "Film Art"
            ]
        }
    },
    "Seoul National University": {
        "korean_track": {
            "College of Humanities": [
                "Korean Language and Literature",
                "Chinese Language and Literature",
                "English Language and Literature",
                "French Language and Literature",
                "German Language and Literature",
                "Russian Language and Literature",
                "Hispanic Language and Literature",
                "Linguistics",
                "Asian Languages and Civilizations",
                "History",
                "Archaeology and Art History",
                "Philosophy",
                "Religious Studies",
                "Aesthetics"
            ],
            "College of Social Sciences": [
                "Political Science and International Relations",
                "Economics",
                "Sociology",
                "Anthropology",
                "Psychology",
                "Geography",
                "Social Welfare",
                "Communication",
                "Statistics",
                "Physics & Astronomy (Physics Major)",
                "Physics & Astronomy (Astronomy Major)",
                "Chemistry",
                "Biological Sciences",
                "Earth and Environmental Sciences"
            ],
            "College of Natural Sciences": [
                "Mathematical Sciences"
            ],
            "College of Liberal Studies": [
                "Liberal Studies"
            ],
            "College of Medicine": [
                "Nursing",
                "Veterinary Medicine"
            ],
            "College of Business Administration": [
                "Business Administration"
            ],
            "College of Engineering": [
                "Civil and Environmental Engineering",
                "Mechanical Engineering",
                "Materials Science and Engineering",
                "Electrical and Computer Engineering",
                "Computer Science and Engineering",
                "Chemical and Biological Engineering",
                "Architecture and Architectural Engineering",
                "Industrial Engineering",
                "Energy Resources Engineering",
                "Nuclear Engineering",
                "Naval Architecture and Ocean Engineering",
                "Aerospace Engineering"
            ],
            "College of Agriculture and Life Sciences": [
                "Agricultural and Resource Economics",
                "Regional Information",
                "Crop Science and Biotechnology",
                "Horticultural Science and Biotechnology",
                "Vocational Education and Workforce Development",
                "Forest Environmental Science",
                "Environmental Materials Science",
                "Food Science and Biotechnology",
                "Animal Science and Biotechnology",
                "Applied Life Chemistry",
                "Applied Biology",
                "Landscape Architecture",
                "Rural Systems Engineering",
                "Biosystems Engineering",
                "Biomaterials Engineering"
            ],
            "College of Fine Arts": [
                "Oriental Painting",
                "Painting",
                "Sculpture",
                "Craft Design"
            ],
            "College of Education": [
                "Education Korean Language Education",
                "English Language Education",
                "German Language Education",
                "French Language Education",
                "Social Studies Education",
                "History Education",
                "Geography Education",
                "Ethics Education",
                "Mathematics Education",
                "Physics Education",
                "Chemistry Education",
                "Biology Education",
                "Earth Science Education",
                "Physical Education"
            ],
            "College of Human Ecology": [
                "Consumer and Child Studies (Consumer Science)",
                "Consumer and Child Studies (Child Development and Family Studies)",
                "Food and Nutrition",
                "Fashion and Textiles"
            ],
            "College of Music": [
                "Vocal Music",
                "Composition",
                "Music Piano",
                "Orchestral instruments",
                "Korean Music"
            ]
        },
        "english_track": {
            "Departments": [
                "Please refer to each department`s website to check whether they have English-taught courses. However, in order to graduate from SNU, you will be required to take some courses in Korean."
            ]
        }
    },
    "Sungkyunkwan University": {
        "english_track": {
            "Departments": [
                "Not available"
            ]
        },
        "korean_track": {
            "Humanities": [
                "Confucian and Oriental Studies Korean Language and Literature",
                "English Language and Literature",
                "French Language and Literature",
                "Chinese Language and Literature",
                "German Language and Literature",
                "Russian Language and Literature",
                "Korean Literature in Classical Chinese",
                "History",
                "Philosophy",
                "Library and Information Science"
            ],
            "Social Sciences": [
                "Public Administration",
                "Political Science and Diplomacy",
                "Media and Communication",
                "Sociology",
                "Social Welfare",
                "Psychology",
                "Consumer Sciences",
                "Child Psychology and Education Economics",
                "Statistics"
            ],
            "Natural Sciences": [
                "Biological Sciences",
                "Mathematics",
                "Physics",
                "Chemistry Food Science and Biotechnology",
                "Bio-Mechatronic Engineering",
                "Integrative Biotechnology"
            ],
            "Engineering": [
                "Chemical Engineering/Polymer Science & Engineering",
                "Advanced Materials Science and Engineering",
                "Mechanical Engineering",
                "Civil Architectural Engineering and Landscape Architecture",
                "Systems Management Engineering",
                "Nano Engineering"
            ]
        }
    },
    "UNIST": {
        "english_track": {
            "College of Engineering": [
                "Department of Mechanical Engineering",
                "Department of Urban and Environmental Engineering",
                "Department of Materials Science and Engineering",
                "School of Energy and Chemical Engineering",
                "Department of Nuclear Engineering"
            ],
            "College of Information and Biotechnology": [
                "Department of Design",
                "Department of Biomedical Engineering",
                "Department of Industrial Engineering",
                "Department of Biological Sciences",
                "Department of Electrical Engineering",
                "Department of Computer Science and Engineering"
            ],
            "College of Natural Sciences": [
                "Department of Physics",
                "Department of Mathematical Sciences",
                "Department of Chemistry"
            ]
        },
        "korean_track": {
            "College of Engineering": [
                "Department of Mechanical Engineering",
                "Department of Earth",
                "Environment and Urban Construction Engineering",
                "Department of New Materials Engineering",
                "Department of Energy and Chemical Engineering",
                "Department of Nuclear Engineering",
                "Department of Semiconductor Engineering (Samsung Electronics Contract Department)"
            ],
            "College of Information and Bio Convergence": [
                "Department of Design",
                "Department of Biomedical Engineering",
                "Department of Industrial Engineering",
                "Department of Life Sciences",
                "Department of Electrical and Electronic Engineering"
            ],
            "College of Natural Sciences": [
                "Department of Physics",
                "Department of Mathematical Sciences",
                "Department of Chemistry"
            ]
        }
    },
    "University of Seoul": {
        "english_track": {
            "Departments": [
                "Not available"
            ]
        },
        "korean_track": {
            "Public Affairs and Economics": [
                "Public Administration",
                "International Relations",
                "Social Welfare",
                "Economics",
                "Science in Taxation"
            ],
            "Business Administration": [
                "Business Administration:"
            ],
            "Engineering": [
                "Electrical and Computer Engineering",
                "Chemical Engineering",
                "Mechanical and Information Engineering",
                "New Materials Science and Engineering",
                "Civil Engineering",
                "Computer Science and Engineering",
                "Artificial Intelligence"
            ],
            "Humanities": [
                "English Language and Literature",
                "Korean Language and Literature",
                "Korean History",
                "Philosophy",
                "Chinese Language and Culture"
            ],
            "Natural Science": [
                "Mathematics",
                "Statistics",
                "Physics",
                "Life Sciences",
                "Environmental Horticulture",
                "Applied Chemistry"
            ],
            "Urban Science": [
                "Architecture (five-years)",
                "Architectural Engineering",
                "Urban Planning and Design",
                "Transportation Engineering",
                "Landscape Architecture",
                "Urban Administration",
                "Urban Sociology",
                "Geoinformatics",
                "Environmental Engineering"
            ],
            "Arts and Physical Education": [
                "Music",
                "Design",
                "Sports Science",
                "Environmental Sculpture"
            ]
        }
    },
    "Yonsei Underwood College": {
        "english_track": {
            "International studies": [
                "Comparative Literature and Culture",
                "Economics",
                "International Studies",
                "Political Science and International Relations",
                "Life Science and Biotechnology"
            ],
            "Humanities, Arts, and Social Sciences": [
                "Asian Studies",
                "Information and Interaction Design",
                "Creative Technology Management",
                "Culture and Design Management",
                "Justice and Civil Leadership",
                "Quantitative Risk Management. Science",
                "Technology",
                "and Policy",
                "Sustainable Development and Cooperation"
            ],
            "Integrated Science and Engineering": [
                "Bio-Convergence",
                "Energy and Environmental Science and Engineering",
                "Nano Science and Engineering"
            ]
        },
        "korean_track": {
            "Departments": [
                "Yonsei Underwood International College does not offer courses in Korean."
            ]
        }
    }
}

# Insert the data into the collection
universities_collection.insert_one(data)


