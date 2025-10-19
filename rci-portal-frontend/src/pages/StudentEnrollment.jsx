import { useState } from 'react'
import { 
  BookOpen, 
  Search, 
  Filter,
  Clock,
  User,
  CheckCircle,
  XCircle,
  AlertCircle,
  Calendar,
  MapPin,
  Award
} from 'lucide-react'
import DashboardLayout from '../components/layout/DashboardLayout'
import Card from '../components/ui/Card'
import Button from '../components/ui/Button'
import Input from '../components/ui/Input'
import Modal from '../components/ui/Modal'
import Alert from '../components/ui/Alert'

const StudentEnrollment = () => {
  const [searchQuery, setSearchQuery] = useState('')
  const [selectedYearLevel, setSelectedYearLevel] = useState('all')
  const [selectedSubject, setSelectedSubject] = useState(null)
  const [isEnrollModalOpen, setIsEnrollModalOpen] = useState(false)
  const [enrolledSubjects, setEnrolledSubjects] = useState([])
  const [showSuccessAlert, setShowSuccessAlert] = useState(false)

  // Mock available subjects (will come from API later)
  const availableSubjects = [
    {
      id: 1,
      code: 'CS 301',
      name: 'Data Structures and Algorithms',
      units: 3,
      yearLevel: 3,
      semester: 1,
      schedule: 'MWF 10:00-11:30 AM',
      room: 'CS Lab 1',
      professor: 'Dr. Maria Santos',
      slots: 35,
      enrolled: 28,
      prerequisites: [
        { code: 'CS 201', name: 'Programming II', passed: true },
        { code: 'MATH 201', name: 'Discrete Mathematics', passed: true }
      ],
      description: 'Study of fundamental data structures and algorithms including arrays, linked lists, stacks, queues, trees, and graphs.'
    },
    {
      id: 2,
      code: 'CS 302',
      name: 'Database Management Systems',
      units: 3,
      yearLevel: 3,
      semester: 1,
      schedule: 'TTH 1:00-2:30 PM',
      room: 'CS Lab 2',
      professor: 'Prof. Juan Reyes',
      slots: 40,
      enrolled: 35,
      prerequisites: [
        { code: 'CS 201', name: 'Programming II', passed: true },
        { code: 'CS 202', name: 'Data Structures', passed: false }
      ],
      description: 'Introduction to database concepts, SQL, normalization, and database design principles.'
    },
    {
      id: 3,
      code: 'CS 303',
      name: 'Web Development',
      units: 3,
      yearLevel: 3,
      semester: 1,
      schedule: 'MWF 2:00-3:30 PM',
      room: 'CS Lab 3',
      professor: 'Dr. Anna Garcia',
      slots: 30,
      enrolled: 25,
      prerequisites: [
        { code: 'CS 201', name: 'Programming II', passed: true }
      ],
      description: 'Modern web development techniques including HTML, CSS, JavaScript, and popular frameworks.'
    },
    {
      id: 4,
      code: 'MATH 301',
      name: 'Linear Algebra',
      units: 3,
      yearLevel: 3,
      semester: 1,
      schedule: 'TTH 10:00-11:30 AM',
      room: 'Math Bldg 201',
      professor: 'Dr. Pedro Santos',
      slots: 40,
      enrolled: 30,
      prerequisites: [
        { code: 'MATH 201', name: 'Calculus II', passed: true }
      ],
      description: 'Study of vector spaces, linear transformations, matrices, and determinants.'
    },
    {
      id: 5,
      code: 'CS 304',
      name: 'Software Engineering',
      units: 3,
      yearLevel: 3,
      semester: 1,
      schedule: 'MWF 8:00-9:30 AM',
      room: 'CS Lab 1',
      professor: 'Engr. Lisa Cruz',
      slots: 35,
      enrolled: 32,
      prerequisites: [
        { code: 'CS 201', name: 'Programming II', passed: true },
        { code: 'CS 202', name: 'Data Structures', passed: false }
      ],
      description: 'Software development lifecycle, project management, design patterns, and best practices.'
    }
  ]

  // Filter subjects based on search and year level
  const filteredSubjects = availableSubjects.filter(subject => {
    const matchesSearch = subject.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         subject.code.toLowerCase().includes(searchQuery.toLowerCase())
    const matchesYear = selectedYearLevel === 'all' || subject.yearLevel === parseInt(selectedYearLevel)
    return matchesSearch && matchesYear
  })

  const canEnroll = (subject) => {
    const allPrereqsPassed = subject.prerequisites.every(prereq => prereq.passed)
    const hasSlots = subject.enrolled < subject.slots
    const notAlreadyEnrolled = !enrolledSubjects.includes(subject.id)
    return allPrereqsPassed && hasSlots && notAlreadyEnrolled
  }

  const handleEnrollClick = (subject) => {
    setSelectedSubject(subject)
    setIsEnrollModalOpen(true)
  }

  const handleConfirmEnroll = () => {
    if (selectedSubject) {
      setEnrolledSubjects([...enrolledSubjects, selectedSubject.id])
      setIsEnrollModalOpen(false)
      setShowSuccessAlert(true)
      setTimeout(() => setShowSuccessAlert(false), 5000)
    }
  }

  const getPrereqStatus = (prerequisites) => {
    const passed = prerequisites.filter(p => p.passed).length
    const total = prerequisites.length
    
    if (passed === total) {
      return { color: 'text-green-600', bg: 'bg-green-100', icon: CheckCircle, text: 'All prerequisites met' }
    } else {
      return { color: 'text-red-600', bg: 'bg-red-100', icon: XCircle, text: `${total - passed} prerequisite(s) not met` }
    }
  }

  return (
    <DashboardLayout>
      <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 p-6">
        <div className="max-w-7xl mx-auto">
          {/* Header */}
          <div className="mb-6">
            <h1 className="text-3xl font-bold text-gray-900 mb-2">Subject Enrollment</h1>
            <p className="text-gray-600">Browse and enroll in available subjects for this semester</p>
          </div>

          {/* Success Alert */}
          {showSuccessAlert && (
            <div className="mb-6">
              <Alert
                type="success"
                title="Enrollment Successful!"
                message={`You have successfully enrolled in ${selectedSubject?.code} - ${selectedSubject?.name}`}
                onClose={() => setShowSuccessAlert(false)}
              />
            </div>
          )}

          {/* Filters & Search */}
          <Card className="mb-6">
            <Card.Content className="p-4">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {/* Search */}
                <div className="md:col-span-2">
                  <div className="relative">
                    <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
                    <Input
                      type="text"
                      placeholder="Search by subject code or name..."
                      value={searchQuery}
                      onChange={(e) => setSearchQuery(e.target.value)}
                      className="pl-10"
                    />
                  </div>
                </div>

                {/* Year Level Filter */}
                <div>
                  <select
                    value={selectedYearLevel}
                    onChange={(e) => setSelectedYearLevel(e.target.value)}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="all">All Year Levels</option>
                    <option value="1">1st Year</option>
                    <option value="2">2nd Year</option>
                    <option value="3">3rd Year</option>
                    <option value="4">4th Year</option>
                  </select>
                </div>
              </div>
            </Card.Content>
          </Card>

          {/* Summary Stats */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
            <Card>
              <Card.Content className="p-4 flex items-center gap-3">
                <div className="p-3 bg-blue-100 rounded-lg">
                  <BookOpen className="w-6 h-6 text-blue-600" />
                </div>
                <div>
                  <p className="text-2xl font-bold text-gray-900">{availableSubjects.length}</p>
                  <p className="text-xs text-gray-600">Available Subjects</p>
                </div>
              </Card.Content>
            </Card>

            <Card>
              <Card.Content className="p-4 flex items-center gap-3">
                <div className="p-3 bg-green-100 rounded-lg">
                  <CheckCircle className="w-6 h-6 text-green-600" />
                </div>
                <div>
                  <p className="text-2xl font-bold text-gray-900">{enrolledSubjects.length}</p>
                  <p className="text-xs text-gray-600">Enrolled This Session</p>
                </div>
              </Card.Content>
            </Card>

            <Card>
              <Card.Content className="p-4 flex items-center gap-3">
                <div className="p-3 bg-purple-100 rounded-lg">
                  <Award className="w-6 h-6 text-purple-600" />
                </div>
                <div>
                  <p className="text-2xl font-bold text-gray-900">
                    {enrolledSubjects.reduce((sum, id) => {
                      const subject = availableSubjects.find(s => s.id === id)
                      return sum + (subject?.units || 0)
                    }, 0)}
                  </p>
                  <p className="text-xs text-gray-600">Total Units</p>
                </div>
              </Card.Content>
            </Card>

            <Card>
              <Card.Content className="p-4 flex items-center gap-3">
                <div className="p-3 bg-orange-100 rounded-lg">
                  <AlertCircle className="w-6 h-6 text-orange-600" />
                </div>
                <div>
                  <p className="text-2xl font-bold text-gray-900">
                    {availableSubjects.filter(s => !canEnroll(s) && !enrolledSubjects.includes(s.id)).length}
                  </p>
                  <p className="text-xs text-gray-600">Unavailable</p>
                </div>
              </Card.Content>
            </Card>
          </div>

          {/* Subject List */}
          <div className="space-y-4">
            {filteredSubjects.length === 0 ? (
              <Card>
                <Card.Content className="p-8 text-center">
                  <BookOpen className="w-16 h-16 text-gray-400 mx-auto mb-4" />
                  <p className="text-gray-600">No subjects found matching your criteria</p>
                </Card.Content>
              </Card>
            ) : (
              filteredSubjects.map(subject => {
                const canEnrollInSubject = canEnroll(subject)
                const isEnrolled = enrolledSubjects.includes(subject.id)
                const prereqStatus = getPrereqStatus(subject.prerequisites)
                const PrereqIcon = prereqStatus.icon

                return (
                  <Card key={subject.id} className="hover:shadow-lg transition-shadow">
                    <Card.Content className="p-6">
                      <div className="flex flex-col lg:flex-row gap-6">
                        {/* Left: Subject Info */}
                        <div className="flex-1">
                          <div className="flex items-start justify-between mb-3">
                            <div>
                              <div className="flex items-center gap-3 mb-2">
                                <span className="px-3 py-1 bg-blue-100 text-blue-700 text-sm font-semibold rounded">
                                  {subject.code}
                                </span>
                                <span className="text-xs text-gray-500">
                                  {subject.units} units
                                </span>
                              </div>
                              <h3 className="text-xl font-bold text-gray-900 mb-1">
                                {subject.name}
                              </h3>
                              <p className="text-sm text-gray-600 mb-3">
                                {subject.description}
                              </p>
                            </div>
                          </div>

                          {/* Details Grid */}
                          <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mb-4">
                            <div className="flex items-center gap-2 text-sm">
                              <Clock className="w-4 h-4 text-gray-400" />
                              <span className="text-gray-700">{subject.schedule}</span>
                            </div>
                            <div className="flex items-center gap-2 text-sm">
                              <User className="w-4 h-4 text-gray-400" />
                              <span className="text-gray-700">{subject.professor}</span>
                            </div>
                            <div className="flex items-center gap-2 text-sm">
                              <MapPin className="w-4 h-4 text-gray-400" />
                              <span className="text-gray-700">{subject.room}</span>
                            </div>
                            <div className="flex items-center gap-2 text-sm">
                              <Calendar className="w-4 h-4 text-gray-400" />
                              <span className="text-gray-700">
                                Slots: {subject.enrolled}/{subject.slots}
                              </span>
                            </div>
                          </div>

                          {/* Prerequisites */}
                          <div>
                            <div className="flex items-center gap-2 mb-2">
                              <PrereqIcon className={`w-5 h-5 ${prereqStatus.color}`} />
                              <span className={`text-sm font-medium ${prereqStatus.color}`}>
                                {prereqStatus.text}
                              </span>
                            </div>
                            <div className="flex flex-wrap gap-2">
                              {subject.prerequisites.map((prereq, index) => (
                                <span
                                  key={index}
                                  className={`px-2 py-1 text-xs font-medium rounded ${
                                    prereq.passed
                                      ? 'bg-green-100 text-green-700'
                                      : 'bg-red-100 text-red-700'
                                  }`}
                                >
                                  {prereq.passed ? '✓' : '✗'} {prereq.code}
                                </span>
                              ))}
                            </div>
                          </div>
                        </div>

                        {/* Right: Action Button */}
                        <div className="flex items-center">
                          {isEnrolled ? (
                            <div className="text-center">
                              <CheckCircle className="w-12 h-12 text-green-600 mx-auto mb-2" />
                              <span className="text-sm font-medium text-green-600">Enrolled</span>
                            </div>
                          ) : canEnrollInSubject ? (
                            <Button
                              onClick={() => handleEnrollClick(subject)}
                              className="whitespace-nowrap"
                            >
                              Enroll Now
                            </Button>
                          ) : (
                            <Button variant="secondary" disabled>
                              {subject.enrolled >= subject.slots ? 'Full' : 'Prerequisites Not Met'}
                            </Button>
                          )}
                        </div>
                      </div>
                    </Card.Content>
                  </Card>
                )
              })
            )}
          </div>
        </div>
      </div>

      {/* Enrollment Confirmation Modal */}
      <Modal
        isOpen={isEnrollModalOpen}
        onClose={() => setIsEnrollModalOpen(false)}
        title="Confirm Enrollment"
        size="md"
      >
        {selectedSubject && (
          <div className="space-y-4">
            <div className="p-4 bg-blue-50 rounded-lg">
              <h3 className="text-lg font-bold text-gray-900 mb-1">
                {selectedSubject.code} - {selectedSubject.name}
              </h3>
              <p className="text-sm text-gray-600">{selectedSubject.professor}</p>
            </div>

            <div className="space-y-2">
              <div className="flex justify-between text-sm">
                <span className="text-gray-600">Schedule:</span>
                <span className="font-medium">{selectedSubject.schedule}</span>
              </div>
              <div className="flex justify-between text-sm">
                <span className="text-gray-600">Room:</span>
                <span className="font-medium">{selectedSubject.room}</span>
              </div>
              <div className="flex justify-between text-sm">
                <span className="text-gray-600">Units:</span>
                <span className="font-medium">{selectedSubject.units}</span>
              </div>
            </div>

            <Alert
              type="info"
              message="Please review the subject details before confirming your enrollment."
            />

            <div className="flex gap-3 justify-end pt-4 border-t">
              <Button
                variant="secondary"
                onClick={() => setIsEnrollModalOpen(false)}
              >
                Cancel
              </Button>
              <Button onClick={handleConfirmEnroll}>
                Confirm Enrollment
              </Button>
            </div>
          </div>
        )}
      </Modal>
    </DashboardLayout>
  )
}

export default StudentEnrollment