{
    'name' : 'Hospital Management System',
    'author':'Prasiddh Mori',
    'website':'www.gvphospital.org',
    'category':'Government Hospital',
    'summary':'Odoo  16 development of Hospital',
    'depends':['mail'],
    'data':[
        'security\ir.model.access.csv',
        'data\sequence.xml',
        'views\menu.xml',
        'views\patient.xml',
        'views\doctor.xml',
        'wizards\cancel_appointment.xml',
        'reports\patient_template.xml',
        'reports\hospital_report.xml',

    ],
    'installable':True,
    'application':True,
    'auto_install':False
}
