import { useState } from 'react'
import { 
  User, 
  Mail, 
  Phone, 
  MapPin, 
  Calendar,
  GraduationCap,
  BookOpen,
  Award,
  Edit,
  Save,
  X
} from 'lucide-react'
import DashboardLayout from '../components/layout/DashboardLayout'
import useAuthStore from '../store/useAuthStore'
import Card from '../components/ui/Card'
import Button from '../components/ui/Button'
import Input from '../components/ui/Input'
import Modal from '../components/ui/Modal'

const StudentProfile = () => {
  const user = useAuthStore((state) => state.user)
  const [isEditModalOpen, setIsEditModalOpen] = useState(false)
  const [isLoading, setIsLoading] = useState(false)

  // Mock student data (will come from API later)
  const [studentData, setStudentData] = useState({
    studentId: '2021-00123',
    firstName: 'Juan',
    lastName: 'Dela Cruz',
    middleName: 'Santos',
    email: 'juan.delacruz@rci.edu',
    phone: '+63 912 345 6789',
    address: '123 Main St, Manila, Philippines',
    birthDate: '2003-05-15',
    gender: 'Male',
    
    // Program info
    program: 'Bachelor of Science in Computer Science',
    programCode: 'BSCS',
    yearLevel: '3rd Year',
    semester: '1st Semester',
    section: 'CS 3-A',
    academicYear: '2025-2026',
    
    // Academic summary
    gpa: 3.45,
    unitsCompleted: 84,
    totalUnits: 120,
    status: 'Regular',
    dateEnrolled: 'June 2021',
  })

  const [editForm, setEditForm] = useState({
    email: studentData.email,
    phone: studentData.phone,
    address: studentData.address,
  })

  const handleEditChange = (e) => {
    const { name, value } = e.target
    setEditForm(prev => ({ ...prev, [name]: value }))
  }

  const handleSaveProfile = async () => {
    setIsLoading(true)
    
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    // Update student data
    setStudentData(prev => ({
      ...prev,
      email: editForm.email,
      phone: editForm.phone,
      address: editForm.address,
    }))
    
    setIsLoading(false)
    setIsEditModalOpen(false)
    
    // Show success message (you can add a toast notification here)
    alert('Profile updated successfully!')
  }

  const InfoRow = ({ icon: Icon, label, value }) => (
    <div className="flex items-start gap-3 py-3 border-b border-gray-100 last:border-0">
      <div className="p-2 bg-blue-50 rounded-lg">
        <Icon className="w-4 h-4 text-blue-600" />
      </div>
      <div className="flex-1">
        <p className="text-xs text-gray-500 mb-1">{label}</p>
        <p className="text-sm font-medium text-gray-900">{value}</p>
      </div>
    </div>
  )

  const StatCard = ({ icon: Icon, label, value, color, bgColor }) => (
    <div className="bg-white rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow">
      <div className="flex items-center gap-3">
        <div className={`p-3 ${bgColor} rounded-lg`}>
          <Icon className={`w-6 h-6 ${color}`} />
        </div>
        <div>
          <p className="text-2xl font-bold text-gray-900">{value}</p>
          <p className="text-xs text-gray-600">{label}</p>
        </div>
      </div>
    </div>
  )

  return (
    <DashboardLayout>
      <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 p-6">
        <div className="max-w-7xl mx-auto">
          {/* Header */}
          <div className="mb-6">
            <h1 className="text-3xl font-bold text-gray-900 mb-2">My Profile</h1>
            <p className="text-gray-600">View and manage your student information</p>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {/* Left Column - Profile Card */}
            <div className="lg:col-span-1">
              <Card>
                <Card.Content className="p-6">
                  {/* Profile Photo */}
                  <div className="flex flex-col items-center mb-6">
                    <div className="w-32 h-32 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-full flex items-center justify-center mb-4 shadow-lg">
                      <span className="text-4xl font-bold text-white">
                        {studentData.firstName.charAt(0)}{studentData.lastName.charAt(0)}
                      </span>
                    </div>
                    <h2 className="text-2xl font-bold text-gray-900 text-center">
                      {studentData.firstName} {studentData.lastName}
                    </h2>
                    <p className="text-sm text-gray-600 mb-1">{studentData.studentId}</p>
                    <span className="px-3 py-1 bg-green-100 text-green-700 text-xs font-semibold rounded-full">
                      {studentData.status}
                    </span>
                  </div>

                  {/* Quick Info */}
                  <div className="space-y-1">
                    <InfoRow 
                      icon={Mail} 
                      label="Email" 
                      value={studentData.email} 
                    />
                    <InfoRow 
                      icon={Phone} 
                      label="Phone" 
                      value={studentData.phone} 
                    />
                    <InfoRow 
                      icon={MapPin} 
                      label="Address" 
                      value={studentData.address} 
                    />
                    <InfoRow 
                      icon={Calendar} 
                      label="Birth Date" 
                      value={new Date(studentData.birthDate).toLocaleDateString('en-US', { 
                        year: 'numeric', 
                        month: 'long', 
                        day: 'numeric' 
                      })} 
                    />
                  </div>

                  {/* Edit Button */}
                  <Button 
                    className="w-full mt-6"
                    onClick={() => {
                      setEditForm({
                        email: studentData.email,
                        phone: studentData.phone,
                        address: studentData.address,
                      })
                      setIsEditModalOpen(true)
                    }}
                  >
                    <Edit className="w-4 h-4 mr-2" />
                    Edit Profile
                  </Button>
                </Card.Content>
              </Card>
            </div>

            {/* Right Column - Program & Academic Info */}
            <div className="lg:col-span-2 space-y-6">
              {/* Academic Summary Stats */}
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <StatCard
                  icon={Award}
                  label="Current GPA"
                  value={studentData.gpa.toFixed(2)}
                  color="text-green-600"
                  bgColor="bg-green-100"
                />
                <StatCard
                  icon={BookOpen}
                  label="Units Completed"
                  value={`${studentData.unitsCompleted}/${studentData.totalUnits}`}
                  color="text-blue-600"
                  bgColor="bg-blue-100"
                />
                <StatCard
                  icon={GraduationCap}
                  label="Year Level"
                  value={studentData.yearLevel}
                  color="text-purple-600"
                  bgColor="bg-purple-100"
                />
              </div>

              {/* Program Information */}
              <Card>
                <Card.Header>
                  <Card.Title className="flex items-center gap-2">
                    <GraduationCap className="w-6 h-6 text-blue-600" />
                    Program Information
                  </Card.Title>
                </Card.Header>
                <Card.Content>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <label className="text-xs text-gray-500 font-medium">Program</label>
                      <p className="text-lg font-semibold text-gray-900 mt-1">
                        {studentData.program}
                      </p>
                      <p className="text-sm text-gray-600">({studentData.programCode})</p>
                    </div>
                    
                    <div>
                      <label className="text-xs text-gray-500 font-medium">Current Section</label>
                      <p className="text-lg font-semibold text-gray-900 mt-1">
                        {studentData.section}
                      </p>
                    </div>

                    <div>
                      <label className="text-xs text-gray-500 font-medium">Academic Year</label>
                      <p className="text-lg font-semibold text-gray-900 mt-1">
                        {studentData.academicYear}
                      </p>
                    </div>

                    <div>
                      <label className="text-xs text-gray-500 font-medium">Current Semester</label>
                      <p className="text-lg font-semibold text-gray-900 mt-1">
                        {studentData.semester}
                      </p>
                    </div>

                    <div>
                      <label className="text-xs text-gray-500 font-medium">Date Enrolled</label>
                      <p className="text-lg font-semibold text-gray-900 mt-1">
                        {studentData.dateEnrolled}
                      </p>
                    </div>

                    <div>
                      <label className="text-xs text-gray-500 font-medium">Student Status</label>
                      <p className="text-lg font-semibold text-gray-900 mt-1">
                        {studentData.status}
                      </p>
                    </div>
                  </div>
                </Card.Content>
              </Card>

              {/* Personal Information */}
              <Card>
                <Card.Header>
                  <Card.Title className="flex items-center gap-2">
                    <User className="w-6 h-6 text-blue-600" />
                    Personal Information
                  </Card.Title>
                </Card.Header>
                <Card.Content>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <label className="text-xs text-gray-500 font-medium">First Name</label>
                      <p className="text-sm font-medium text-gray-900 mt-1">
                        {studentData.firstName}
                      </p>
                    </div>

                    <div>
                      <label className="text-xs text-gray-500 font-medium">Last Name</label>
                      <p className="text-sm font-medium text-gray-900 mt-1">
                        {studentData.lastName}
                      </p>
                    </div>

                    <div>
                      <label className="text-xs text-gray-500 font-medium">Middle Name</label>
                      <p className="text-sm font-medium text-gray-900 mt-1">
                        {studentData.middleName}
                      </p>
                    </div>

                    <div>
                      <label className="text-xs text-gray-500 font-medium">Gender</label>
                      <p className="text-sm font-medium text-gray-900 mt-1">
                        {studentData.gender}
                      </p>
                    </div>

                    <div className="md:col-span-2">
                      <label className="text-xs text-gray-500 font-medium">Complete Address</label>
                      <p className="text-sm font-medium text-gray-900 mt-1">
                        {studentData.address}
                      </p>
                    </div>
                  </div>
                </Card.Content>
              </Card>

              {/* Academic Progress */}
              <Card>
                <Card.Header>
                  <Card.Title className="flex items-center gap-2">
                    <BookOpen className="w-6 h-6 text-blue-600" />
                    Academic Progress
                  </Card.Title>
                </Card.Header>
                <Card.Content>
                  <div className="space-y-4">
                    <div>
                      <div className="flex justify-between text-sm mb-2">
                        <span className="text-gray-600">Units Completed</span>
                        <span className="font-semibold text-gray-900">
                          {studentData.unitsCompleted} / {studentData.totalUnits} units
                        </span>
                      </div>
                      <div className="w-full bg-gray-200 rounded-full h-3">
                        <div 
                          className="bg-gradient-to-r from-blue-500 to-blue-600 h-3 rounded-full transition-all duration-500"
                          style={{ width: `${(studentData.unitsCompleted / studentData.totalUnits) * 100}%` }}
                        ></div>
                      </div>
                      <p className="text-xs text-gray-500 mt-1">
                        {studentData.totalUnits - studentData.unitsCompleted} units remaining to graduate
                      </p>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pt-4 border-t">
                      <div>
                        <p className="text-xs text-gray-500 mb-1">Estimated Graduation</p>
                        <p className="text-lg font-semibold text-gray-900">June 2026</p>
                      </div>
                      <div>
                        <p className="text-xs text-gray-500 mb-1">Academic Standing</p>
                        <span className="inline-block px-3 py-1 bg-green-100 text-green-700 text-sm font-semibold rounded-full">
                          Good Standing
                        </span>
                      </div>
                    </div>
                  </div>
                </Card.Content>
              </Card>
            </div>
          </div>
        </div>
      </div>

      {/* Edit Profile Modal */}
      <Modal
        isOpen={isEditModalOpen}
        onClose={() => setIsEditModalOpen(false)}
        title="Edit Profile"
        size="md"
      >
        <div className="space-y-4">
          <Input
            label="Email Address"
            type="email"
            name="email"
            value={editForm.email}
            onChange={handleEditChange}
            placeholder="your.email@rci.edu"
          />

          <Input
            label="Phone Number"
            type="tel"
            name="phone"
            value={editForm.phone}
            onChange={handleEditChange}
            placeholder="+63 XXX XXX XXXX"
          />

          <Input
            label="Address"
            type="text"
            name="address"
            value={editForm.address}
            onChange={handleEditChange}
            placeholder="Complete address"
          />

          <div className="pt-4 border-t flex gap-3 justify-end">
            <Button
              variant="secondary"
              onClick={() => setIsEditModalOpen(false)}
              disabled={isLoading}
            >
              <X className="w-4 h-4 mr-2" />
              Cancel
            </Button>
            <Button
              onClick={handleSaveProfile}
              disabled={isLoading}
            >
              <Save className="w-4 h-4 mr-2" />
              {isLoading ? 'Saving...' : 'Save Changes'}
            </Button>
          </div>
        </div>
      </Modal>
    </DashboardLayout>
  )
}

export default StudentProfile