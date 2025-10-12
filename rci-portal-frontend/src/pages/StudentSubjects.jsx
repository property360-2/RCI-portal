import { useState } from 'react'
import { BookOpen, FileText, Eye } from 'lucide-react'
import DashboardLayout from '../components/layout/DashboardLayout'
import Card from '../components/ui/Card'
import Table from '../components/ui/Table'
import Button from '../components/ui/Button'
import Modal from '../components/ui/Modal'
import Alert from '../components/ui/Alert'
import { LoadingSpinner } from '../components/ui/Loading'

const StudentSubjects = () => {
  const [selectedSubject, setSelectedSubject] = useState(null)
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [loading, setLoading] = useState(false)

  // Sample data - replace with API call
  const subjects = [
    {
      id: 1,
      code: 'IT101',
      title: 'Introduction to Programming',
      units: 3,
      schedule: 'MWF 8:00-9:00 AM',
      room: 'IT-301',
      professor: 'Prof. Juan Dela Cruz',
    },
    {
      id: 2,
      code: 'IT102',
      title: 'Database Management',
      units: 3,
      schedule: 'TTH 10:00-11:30 AM',
      room: 'IT-302',
      professor: 'Prof. Maria Santos',
    },
    {
      id: 3,
      code: 'IT103',
      title: 'Web Development',
      units: 3,
      schedule: 'MWF 1:00-2:00 PM',
      room: 'IT-303',
      professor: 'Prof. Pedro Reyes',
    },
  ]

  const handleViewSyllabus = (subject) => {
    setSelectedSubject(subject)
    setIsModalOpen(true)
  }

  return (
    <DashboardLayout>
      <div className="p-6">
        <div className="max-w-7xl mx-auto">
          {/* Header */}
          <div className="mb-6">
            <h1 className="text-3xl font-bold text-gray-900 mb-2">
              My Subjects
            </h1>
            <p className="text-gray-600">
              View your enrolled subjects for this semester
            </p>
          </div>

          {/* Info Alert */}
          <Alert
            type="info"
            title="Academic Year 2024-2025"
            message="You are currently enrolled in 7 subjects for the 1st Semester"
            className="mb-6"
          />

          {/* Stats Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <Card>
              <Card.Content className="flex items-center gap-4">
                <div className="p-3 bg-primary-100 rounded-full">
                  <BookOpen className="w-6 h-6 text-primary-600" />
                </div>
                <div>
                  <p className="text-sm text-gray-600">Total Subjects</p>
                  <p className="text-2xl font-bold">{subjects.length}</p>
                </div>
              </Card.Content>
            </Card>

            <Card>
              <Card.Content className="flex items-center gap-4">
                <div className="p-3 bg-green-100 rounded-full">
                  <FileText className="w-6 h-6 text-green-600" />
                </div>
                <div>
                  <p className="text-sm text-gray-600">Total Units</p>
                  <p className="text-2xl font-bold">
                    {subjects.reduce((sum, s) => sum + s.units, 0)}
                  </p>
                </div>
              </Card.Content>
            </Card>

            <Card>
              <Card.Content className="flex items-center gap-4">
                <div className="p-3 bg-blue-100 rounded-full">
                  <Eye className="w-6 h-6 text-blue-600" />
                </div>
                <div>
                  <p className="text-sm text-gray-600">Attendance Rate</p>
                  <p className="text-2xl font-bold">95%</p>
                </div>
              </Card.Content>
            </Card>
          </div>

          {/* Subjects Table */}
          <Card>
            <Card.Header>
              <Card.Title>Enrolled Subjects</Card.Title>
            </Card.Header>
            <Card.Content className="p-0">
              {loading ? (
                <div className="flex items-center justify-center py-12">
                  <LoadingSpinner size="lg" />
                </div>
              ) : (
                <Table>
                  <Table.Header>
                    <Table.Row>
                      <Table.Head>Code</Table.Head>
                      <Table.Head>Subject Title</Table.Head>
                      <Table.Head>Units</Table.Head>
                      <Table.Head>Schedule</Table.Head>
                      <Table.Head>Room</Table.Head>
                      <Table.Head>Professor</Table.Head>
                      <Table.Head>Actions</Table.Head>
                    </Table.Row>
                  </Table.Header>
                  <Table.Body>
                    {subjects.map((subject) => (
                      <Table.Row key={subject.id}>
                        <Table.Cell>
                          <span className="font-semibold text-primary-600">
                            {subject.code}
                          </span>
                        </Table.Cell>
                        <Table.Cell>{subject.title}</Table.Cell>
                        <Table.Cell>{subject.units}</Table.Cell>
                        <Table.Cell>{subject.schedule}</Table.Cell>
                        <Table.Cell>{subject.room}</Table.Cell>
                        <Table.Cell>{subject.professor}</Table.Cell>
                        <Table.Cell>
                          <Button
                            size="sm"
                            variant="outline"
                            onClick={() => handleViewSyllabus(subject)}
                          >
                            <FileText className="w-4 h-4 mr-1" />
                            Syllabus
                          </Button>
                        </Table.Cell>
                      </Table.Row>
                    ))}
                  </Table.Body>
                </Table>
              )}
            </Card.Content>
          </Card>
        </div>
      </div>

      {/* Syllabus Modal */}
      <Modal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        title={`${selectedSubject?.code} - Syllabus`}
        size="lg"
      >
        <div className="space-y-4">
          <div>
            <h3 className="font-semibold text-gray-900 mb-2">
              {selectedSubject?.title}
            </h3>
            <p className="text-sm text-gray-600">
              Professor: {selectedSubject?.professor}
            </p>
          </div>

          <div className="border-t pt-4">
            <p className="text-gray-700">
              Syllabus content will be displayed here...
            </p>
            <p className="text-sm text-gray-500 mt-2">
              This would typically load a PDF or detailed course outline.
            </p>
          </div>
        </div>

        <Modal.Footer>
          <Button variant="outline" onClick={() => setIsModalOpen(false)}>
            Close
          </Button>
          <Button>
            <FileText className="w-4 h-4 mr-2" />
            Download PDF
          </Button>
        </Modal.Footer>
      </Modal>
    </DashboardLayout>
  )
}

export default StudentSubjects